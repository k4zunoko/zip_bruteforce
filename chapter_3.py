import pyzipper
import itertools
import time

def extract_zip(password):
    with pyzipper.AESZipFile(zip_file_name) as zip_file:
        try:
            zip_file.pwd = password.encode()
            zip_file.extractall()
            return True
        except Exception:
            return False

start_time = time.time()
count = 0  # 解析したパスワード数をカウントするリスト
progress = 0

# 解析するzipファイル名
zip_file_name = f"storage/{input('解析するzipファイル名（拡張子なし）= ')}.zip"

# 解析するパスワードの桁数
password_length = 3
charset = "abcdefghijklmnopqrstuvwxyz"
passwords = list(itertools.product(charset, repeat=password_length))
total_passwords = len(charset) ** password_length

print(f"{password_length}ケタ")

# パスワードの総当たりを行う
for password in passwords:
    password = "".join(password)
    count += 1
    if extract_zip(password):
        print(f"Success! Password is {password}")
        break
    progress = int(count / total_passwords * 100)
    print(f"Progress: {progress}%")

end_time = time.time()
elapsed_time = int(end_time - start_time)
print(f"Elapsed time: {elapsed_time} seconds")