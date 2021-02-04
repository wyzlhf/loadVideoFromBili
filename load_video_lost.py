import os


def load_lost_video(base_url, out_put_path, lost_list):
    video_url = base_url + '?p='
    while lost_list:
        for i in lost_list:
            try:
                command_word = "you-get -o " + out_put_path + " " + video_url + str(i)
                os.system(command_word)
                del lost_list[i]
            except:
                lost_list.append(lost_list[i])



if __name__ == '__main__':
    base_url = 'https://www.bilibili.com/video/BV1R7411F7JV'
    out_put_path = r"D:\Video\Python全套视频教程（700集）"
    lost_list = [232, 254, 343, 478, 571, 579]
    load_lost_video(
        base_url,
        out_put_path,
        lost_list
    )
