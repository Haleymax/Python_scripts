import os
import shutil


def delete_folders_with_numbers(directory):
    # 获取当前目录下的所有文件和文件夹
    items = os.listdir(directory)

    # 遍历所有项目
    for item in items:
        # 检查项目是否为文件夹并且名字为数字1到99
        if os.path.isdir(os.path.join(directory, item)) and item.isdigit() and 1 <= int(item) <= 99:
            folder_path = os.path.join(directory, item)
            try:
                # 删除文件夹及其内容
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path}")
            except Exception as e:
                print(f"Error deleting folder {folder_path}: {e}")


if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    delete_folders_with_numbers(current_directory)