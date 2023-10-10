import os
import subprocess


pass_word = input("ファイル名=")
print(pass_word)

input_dir_path = os.path.join(os.path.dirname(__file__), "storage/sample.txt") # 圧縮対象フォルダ
output_dir_path = os.path.join(os.path.dirname(__file__), "storage") # 圧縮後のフォルダ

path_exe = r'C:\Program Files\7-Zip\7z.exe'# 7zip実行ファイルのパス
args = (
       path_exe, 
       'a', 
       os.path.join(output_dir_path, pass_word+'.zip'), # 圧縮後のファイル
       input_dir_path, # 圧縮対象フォルダ
       '-mx=9', # 圧縮レベル0-9 ９が最大
       '-p=' + pass_word, # パスワード
)

result = subprocess.run(args)