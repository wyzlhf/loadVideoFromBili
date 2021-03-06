import os

path = r"D:\Video\思想实验室——哲学\【邓晓芒】《精神现象学》句读_（全290讲）"


def the_fist_rename():
    for file in os.listdir(path):
        file_name = os.path.join(path, file)
        new_file_name = os.path.join(path, file)\
            .replace("西方哲学思想史【持缓更新中/中英】- the great ideas of philosophy 01 From the Upanishads to Homer (", "")
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