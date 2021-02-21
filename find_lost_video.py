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
    path = r'D:\Video\牛津大学公开课：康德的纯粹理性批判[第4集]先天综合判断如何成为可能'
    url = 'https://www.bilibili.com/video/BV1ux411m7Tc'

    get_list_video(path, url)
