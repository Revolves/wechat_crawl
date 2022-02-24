
import os


def delete_empty_file(path):
    # 删除空白文件
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.stat(file_path).st_size <= 10:
            os.remove(file_path)

# delete_empty_file('url_file')
