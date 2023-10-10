import pyzipper
import time
import os

start_time = time.time()
# 解析するzipファイル名
zip_file_name = os.path.join(os.path.dirname(__file__), "storage/"+input("解析するzipファイル名（拡張子なし）= ")+".zip")

# 解析するパスワードの桁数
password_length = 4
n = 10**password_length
print(f"{password_length}ケタ")

# パスワードの総当たりを行う
for i in range(n):
    password = "{:04d}".format(i)
    with pyzipper.AESZipFile(zip_file_name, "r") as zip_file:
        try:
            zip_file.pwd = password.encode("utf-8")
            zip_file.extractall()
            print(f"Success! Password is {password}")
            break
        except:
            continue

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
