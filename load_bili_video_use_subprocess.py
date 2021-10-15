import subprocess
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import os
import re

def norm_video_title(video_path):
    file_list=os.listdir(video_path)
    for file_name in file_list:
        old_file_name=video_path+'/'+file_name
        pre_replace_text=re.findall("^.+\(P",old_file_name)[0][:-1]
        try:
            after_replace_text=re.findall(r'\)\.',old_file_name)[0]
            new_file_name=old_file_name.replace(pre_replace_text,'').replace(after_replace_text,'.')
        except:
            new_file_name = old_file_name.replace(pre_replace_text, '')
        new_file_name=video_path+'/'+new_file_name
        os.rename(old_file_name,new_file_name)

def get_playlist_title(playlist_url):
    playlist_content=requests.get(playlist_url).text
    soup = BeautifulSoup(playlist_content, 'html.parser')
    title=soup.find_all('h1')[0]['title']
    return title

def del_file(path,file_format='xml'):
    files=os.listdir(path)
    for file in files:
        the_file_format=file.split('.')[-1]
        if the_file_format==file_format:
            os.remove(path+'/'+file)

def creat_folder(folder_path):
    video_path = Path(folder_path.strip())
    if not video_path.exists():
        subprocess.Popen([
            'mkdir',
            folder_path
        ], shell=True).communicate()


# def get_video(vide_url, video_num,out_path=None):
#     if not out_path:
#         playlist_title = get_playlist_title(vide_url)
#         creat_folder(f'./{playlist_title}')
#         subprocess.Popen([
#             'you-get',
#             '--playlist',
#             '-o',
#             './' + playlist_title,
#             vide_url
#         ], shell=True).communicate()
#         video_path='./' + playlist_title
#         norm_video_title(video_path)
#     else:
#         creat_folder(out_path)
#         subprocess.Popen([
#             'you-get',
#             '-o',
#             out_path,
#             f'{vide_url}?p={video_num}'
#         ], shell=True).communicate()
#         norm_video_title(out_path)


def get_video_list(vide_list_url,out_path=None):
    if not out_path:
        playlist_title=get_playlist_title(vide_list_url)
        creat_folder(f'./{playlist_title}')
        subprocess.Popen([
            'you-get',
            '--playlist',
            '-o',
            './'+playlist_title,
            vide_list_url
        ], shell=True).communicate()
        video_path = './' + playlist_title
        norm_video_title(video_path)
        del_file(video_path)
    else:
        creat_folder(out_path)
        subprocess.Popen([
            'you-get',
            '--playlist',
            '-o',
            out_path,
            vide_list_url
        ], shell=True).communicate()
        norm_video_title(out_path)
        del_file(out_path)


if __name__ == '__main__':
    # video_url='https://www.bilibili.com/video/BV1q5411T7x8'
    video_url='https://www.bilibili.com/video/BV1Lf4y1t7Mc'
    path=r'D:\Video\【千锋】网络安全300集全套视频_零基础小白必备教程'
    get_video_list(video_url,out_path=path)