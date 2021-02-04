import os

path = r"D:\Video\[中英字幕]C++数据结构与算法初学者完整课程"


def the_fist_rename():
    for file in os.listdir(path):
        file_name = os.path.join(path, file)
        new_file_name = os.path.join(path, file).replace("(中英字幕) C-- 数据结构与算法初学者完整课程 (", "")
        os.rename(file_name, new_file_name)


def the_second_rename():
    for file in os.listdir(path):
        file_name = os.path.join(path, file)
        new_file_name = os.path.join(path, file).replace(").mp4", ".mp4")
        os.rename(file_name, new_file_name)


def remove_some_type_file(file_path, file_type):
    _path, dirs, filename = os.walk(file_path)
    filenamelist = filename.split('.')
    if filenamelist[-1] == file_type:
        os.remove(os.path.join(file_path, filename))


if __name__ == '__main__':
    the_fist_rename()
    the_second_rename()