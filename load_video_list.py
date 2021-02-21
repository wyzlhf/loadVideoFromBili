# you-get --playlist
import os


def get_list_video(path, url):
    command_word = 'you-get --playlist ' + url + ' -o ' + path
    os.system(command_word)


if __name__ == '__main__':

    path = r'D:\Video\【中英字幕】哈佛大学本科高年级课程Economics_1723：Capital-Markets'
    url = 'https://www.bilibili.com/video/BV1up4y1s77N'

    # path = r'D:\Video\邓晓芒讲康德《判断力批判》'
    # url = 'https://www.bilibili.com/video/BV1H4411v7AS'

    # path = r'D:\Video\邓晓芒讲：古希腊哲学史'
    # url = 'https://www.bilibili.com/video/BV1x4411K75U'
    get_list_video(path, url)
