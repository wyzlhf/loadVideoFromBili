# import os
#
#
# # 下载文件
# def execute_cmd_command(command_word: str):
#     os.system(command_word)
#
#
# def getLostName():
#     wanted_num_list = [x for x in range(1, 1001)]
#     # wanted_num_list=[1,2,3,4,5,6,7,8,9,10]
#     path = r"D:\TDDOWNLOAD\老男孩Python全栈开发29期全套(2020年3月开班)-同步更新"
#     real_num_list = []
#     lost_num = []
#     name_list = os.listdir(path)
#     for name in name_list:
#         num = name.split('.')[0].replace("P", "")
#         real_num_list.append(int(num))
#         # return real_num_list
#     for num in wanted_num_list:
#         if num in real_num_list:
#             pass
#         else:
#             lost_num.append(num)
#     return lost_num
#
#
# def get_video(lost_list):
#     for i in lost_list:
#         # p=26
#         cmd = 'you-get https://www.bilibili.com/video/BV1QE41147hU?p=' + str(i)
#         # cmd = cmd + str(i)
#         execute_cmd_command(cmd)
#
#
# if __name__ == '__main__':
#     lost_list = getLostName()
#     print(lost_list)
#     get_video(lost_list)
# you-get --playlist
import os


def get_list_video(path, url):
    command_word = 'you-get --playlist ' + url + ' -o ' + path
    os.system(command_word)


if __name__ == '__main__':

    path = r'D:\Video\【MIT公开课】14.772发展经济学宏观经济·2013年春（完结·中英字幕·机翻）'
    url = 'https://www.bilibili.com/video/BV1Jy4y1r7xP'

    # path = r'D:\Video\【MIT公开课】RES.LL-005大数据和机器学习中的数学·IAP2020（完结·中英字幕·机翻）'
    # url = 'https://www.bilibili.com/video/BV17k4y1B7kC'

    # path = r'D:\Video\【MIT公开课】15.401金融理论I·2008年秋（完结·中英字幕·机翻）'
    # url = 'https://www.bilibili.com/video/BV1vD4y1d7HT'

    # path = r'D:\Video\【哈佛大学】ECON1152利用大数据解决经济和社会问题|全18讲|中英字幕'
    # url = 'https://www.bilibili.com/video/BV1w7411w74Z'

    # path = r'D:\Video\【MIT公开课】6.S897机器学习之医疗保健·2019年春（完结·中英字幕·机翻）'
    # url = 'https://www.bilibili.com/video/BV1YK4y1E7UK'

    # path = r'D:\Video\强化学习Reinforcement_Learning|Winter2019'
    # url = 'https://www.bilibili.com/video/BV1bb411M7tu'

    # path = r'D:\Video\【MIT课程】深度学习导论(2020)高清合集中英字幕'
    # url = 'https://www.bilibili.com/video/BV1Aa4y1v7W2'

    # path = r'D:\Video\最新React_Native前端进阶系列基础教程（33天全）'
    # url = 'https://www.bilibili.com/video/BV1AK4y1p7dV'

    get_list_video(path, url)
