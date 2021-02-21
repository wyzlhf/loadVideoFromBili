from bs4 import BeautifulSoup

# from .load_video_list import get_list_video
html = open('111.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(html, 'lxml')
a_tag_list = soup.findAll(name='a', attrs={'class', 'title'})
all_title_link = []

import os


def get_list_video(path, url):
    command_word = 'you-get --playlist ' + url + ' -o ' + path
    os.system(command_word)


for a in a_tag_list:
    link = 'https:' + a.get('href')
    title = a.get('title')
    item = {'title': title, 'link': link}
    all_title_link.append(item)
all_item_list = []
for item in all_title_link:
    path = r'D:\Video\青史钩沉\\' + item['title'].replace(' ', '_').replace('/','_')
    url = item['link']
    print(path)
    print(url)
    list_item = {'path': path, 'url': url}
    all_item_list.append(list_item)

for item in all_item_list:
    get_list_video(item['path'], item['url'])
