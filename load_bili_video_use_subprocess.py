import subprocess
from pathlib import Path
import requests
from bs4 import BeautifulSoup

def get_playlist_title(playlist_url):
    playlist_content=requests.get(playlist_url).text
    soup = BeautifulSoup(playlist_content, 'html.parser')
    title=soup.find_all('h1')[0]['title']
    return title

def creat_folder(folder_path):
    video_path = Path(folder_path.strip())
    if not video_path.exists():
        subprocess.Popen([
            'mkdir',
            folder_path
        ], shell=True).communicate()


def get_video(vide_url, video_num,out_path=None):
    if not out_path:
        playlist_title = get_playlist_title(vide_url)
        creat_folder(f'./{playlist_title}')
        subprocess.Popen([
            'you-get',
            '--playlist',
            '-o',
            './' + playlist_title,
            vide_url
        ], shell=True).communicate()
    else:
        creat_folder(out_path)
        subprocess.Popen([
            'you-get',
            '-o',
            out_path,
            f'{vide_url}?p={video_num}'
        ], shell=True).communicate()


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
    else:
        creat_folder(out_path)
        subprocess.Popen([
            'you-get',
            '--playlist',
            '-o',
            out_path,
            vide_list_url
        ], shell=True).communicate()


if __name__ == '__main__':
    # out_path = 'D:\Video\Python 并发编程实战'
    video_url='https://www.bilibili.com/video/BV1bK411A7tV'
    # video_num=13
    # get_video(out_path,video_url,video_num)
    get_video_list(video_url)
    # creat_folder(out_path)
    # get_playlist_title(video_url)
