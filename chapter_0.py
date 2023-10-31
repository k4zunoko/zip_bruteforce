import pyzipper

def extract_zip(password):
    with pyzipper.AESZipFile(zip_file_name) as zip_file:
        try:
            zip_file.pwd = password.encode()
            zip_file.extractall()
            return True
        except Exception:
            return False
        
zip_file_name = "storage/"+input("解析するzipファイル名（拡張子なし）= ")+".zip"
password = input("パスワード = ")

print(extract_zip(password))