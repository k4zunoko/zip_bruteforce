import pyzipper
import threading
import time

def extract_zip(password):
    with pyzipper.AESZipFile(zip_file_name) as zip_file:
        try:
            zip_file.pwd = password.encode()
            zip_file.extractall()
            return True
        except Exception:
            return False
        
# パスワードを生成するジェネレーター関数
def password_generator(start, step):
    for i in range(start, total_passwords, step):
        yield f"{i:0{password_length}d}"

# パスワードを試す関数
def try_password(password):
    global found_password
    if found_password[0]:
        # すでに正しいパスワードが見つかっている場合は何もしない
        return
    if extract_zip(password):
        found_password[0] = password

start_time = time.time()

# 解析するzipファイル名
zip_file_name = f"storage/{input('解析するzipファイル名（拡張子なし）= ')}.zip"

# 解析するパスワードの桁数
password_length = 3
total_passwords = 10**password_length

print(f"{password_length}ケタ")

# スレッド数
num_threads = 4

# 正しいパスワードが見つかったらここに格納
found_password = [None]



# マルチスレッドでパスワードを試す
threads = []
for i in range(num_threads):
    passwords = password_generator(i, num_threads)
    thread = threading.Thread(target=lambda: [try_password(password) for password in passwords])
    threads.append(thread)
    thread.start()

# スレッドが終了するまで待つ
while any(t.is_alive() for t in threads):
    if found_password[0]:
        # 正しいパスワードが見つかっている場合は、スレッドをすべて終了する
        break
    else:
        print("実行中...")
        time.sleep(1)

print(f"Success! Password is {found_password[0]}")

end_time = time.time()
elapsed_time = int(end_time - start_time)
print(f"Elapsed time: {elapsed_time} seconds")