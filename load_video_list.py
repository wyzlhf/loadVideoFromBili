# you-get --playlist
import os


def get_list_video(path, url):
    command_word = 'you-get --playlist ' + url + ' -o ' + path
    os.system(command_word)


if __name__ == '__main__':
    path = r'D:\Video\【MIT公开课】6.851高级数据结构（完结·中英字幕·机翻)'
    url = 'https://www.bilibili.com/video/BV1iE411n7yJ'

    # path = r'D:\Video\【斯坦福大学】CS246大数据挖掘·2019年（完结·中英字幕·机翻）'
    # url = 'https://www.bilibili.com/video/BV1SC4y187x1'

    # path = r'D:\Video\【公开课】哈佛大学：领袖心理学（中英字幕）'
    # url = 'https://www.bilibili.com/video/BV1Cg4y1b7Y5'

    # path = r'D:\Video\Challenge_Of_The_GoBots百变雄师'
    # url = 'https://www.bilibili.com/video/av11179379'

    # path = r'D:\Video\【斯坦福】CS224W：图机器学习(中英字幕|2019秋)'
    # url = 'https://www.bilibili.com/video/BV1Vg4y1z7Nf'

    # path = r'D:\Video\【CS520】斯坦福大学2020春季知识图谱课程（含中英字幕·自动生成）'
    # url = 'https://www.bilibili.com/video/BV12k4y1R76Q'

    # path = r'D:\Video\[中英字幕]Python神经网络-TensorFlow2.0课程'
    # url = 'https://www.bilibili.com/video/BV125411n7X3'



    get_list_video(path, url)
