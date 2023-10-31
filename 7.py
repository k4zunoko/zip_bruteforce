import pyzipper
import itertools
import threading
import time

start_time = time.time()
# ZIPファイルのパス
zip_file_name = f"storage/{input('解析するzipファイル名（拡張子なし）= ')}.zip"

# スレッドの数（パスワード破解を並列化する場合、適宜変更してください）
num_threads = 4

password_length = 3
charset = "abcdefghijklmnopqrstuvwxyz"
# charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
passwords = list(itertools.product(charset, repeat=password_length))
total_passwords = len(charset) ** password_length
passwords_tried = [0]
chunk_size = total_passwords // num_threads

# 正しいパスワードが見つかったらここに格納
found_password = [None]

def extract_zip(password):
    try:
        with pyzipper.AESZipFile(zip_file_name) as zip_file:
            zip_file.pwd = password.encode()
            zip_file.extractall()
            return True
    except Exception:
        return False
    finally:
        passwords_tried[0] += 1

# パスワードのブルートフォース攻撃
def brute_force_attack(start, end):
    for password in passwords[start:end]:
        password = "".join(password)
        if extract_zip(password):
            found_password[0] = password
            break


threads = []
for i in range(num_threads):
    start = i * chunk_size
    end = start + chunk_size
    t = threading.Thread(target=brute_force_attack, args=(start, end))
    threads.append(t)
    t.start()

# 全てのスレッドの終了を待つ
while any(t.is_alive() for t in threads):
    if found_password[0]:
        # 正しいパスワードが見つかっている場合は、スレッドをすべて終了する
        break
    else:
        # 正しいパスワードが見つかっていない場合は、進捗を表示する
        progress = passwords_tried[0] / total_passwords * 100
        print(f"Progress: {progress:.2f}%")
        time.sleep(1)

progress = passwords_tried[0] / total_passwords * 100
print(f"Progress: {progress:.2f}%")
print(f"Success! Password is {found_password[0]}")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
