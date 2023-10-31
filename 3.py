import pyzipper
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
progress = 0

# 解析するzipファイル名
zip_file_name = f"storage/{input('解析するzipファイル名（拡張子なし）= ')}.zip"

# 解析するパスワードの桁数
password_length = 3
total_passwords = 10**password_length

print(f"{password_length}ケタ")

# パスワードの総当たりを行う
for i in range(total_passwords):
    password = f"{i:0{password_length}d}"
    if extract_zip(password):
        print(f"Success! Password is {password}")
        break
    progress = int(i / total_passwords * 100)
    print(f"Progress: {progress}%")

end_time = time.time()
elapsed_time = int(end_time - start_time)
print(f"Elapsed time: {elapsed_time} seconds")