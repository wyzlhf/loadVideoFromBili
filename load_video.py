import os
from load_video_lost import load_lost_video

def execute_cmd_command(base_url, out_put_path, end_num, start_num=1):
    video_url = base_url + '?p='
    lost_list = []
    for i in range(start_num, end_num):
        try:
            command_word = "you-get -o " + out_put_path + " " + video_url + str(i)
            os.system(command_word)
        except:
            lost_list.append(i)
    return lost_list


if __name__ == '__main__':
    base_url = 'https://www.bilibili.com/video/BV1c4411d7jb'
    out_put_path = r"D:\Video\计算机网络微课堂（有字幕无背景音乐版）"
    start_num = 63
    end_num = 74
    lost_list = execute_cmd_command(
        base_url,
        out_put_path,
        end_num,
        start_num
    )
    load_lost_video(base_url,out_put_path,lost_list)
