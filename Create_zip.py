import os
import pyminizip

pass_word = input("ファイル名=")

input_dir_path = os.path.join(os.path.dirname(__file__), "storage/sample.txt")  # 圧縮対象フォルダ
output_dir_path = os.path.join(os.path.dirname(__file__), "storage")  # 圧縮後のフォルダ
zip_file_path = os.path.join(output_dir_path, pass_word + '.zip')

# ファイルを圧縮
pyminizip.compress(input_dir_path, "", zip_file_path, pass_word, 0)

# 圧縮後のファイルが生成されました
print(f"圧縮完了: {zip_file_path}")

# これで作成したzipファイルはpythonプログラムでうまく解凍できないので使用しない。
# 7zipを用いてAES-256を用いて圧縮したファイルを使用する。