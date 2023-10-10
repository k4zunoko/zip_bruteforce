import pyzipper
import threading
import time
import os

start_time = time.time()

# 解析するzipファイル名
zip_file_name = os.path.join(os.path.dirname(__file__), "storage/"+input("解析するzipファイル名（拡張子なし）= ")+".zip")

# 解析するパスワードの桁数
password_length = 4
n = 10**password_length
count = [0]  # 解析したパスワード数をカウントするリスト

# スレッド数
num_threads = 4

# 正しいパスワードが見つかったらここに格納
found_password = [None]

# パスワードを生成するジェネレーター関数
def password_generator(start, step):
    for i in range(start, n, step):
        yield "{:04d}".format(i)

# パスワードを試す関数
def try_password(password):
    global found_password
    if found_password[0]:
        # すでに正しいパスワードが見つかっている場合は何もしない
        return
    try:
        with pyzipper.AESZipFile(zip_file_name) as zip_file:
            zip_file.pwd = password.encode()
            zip_file.extractall()
            found_password[0] = password
    except:
        pass
    finally:
        count[0] += 1

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
        # 正しいパスワードが見つかっていない場合は、進捗を表示する
        progress = count[0] / n * 100
        print(f"Progress: {progress:.2f}%")
        time.sleep(1)

# 最後に進捗率を表示する
progress = count[0] / n * 100
print(f"Progress: {progress:.2f}%")
print(f"Success! Password is {found_password[0]}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")