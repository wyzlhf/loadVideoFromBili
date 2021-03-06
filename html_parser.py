from bs4 import BeautifulSoup
import os
import requests
from time import sleep
from selenium import webdriver
# from .load_video_list import get_list_video

def get_all_link(page='222.html'):
    html = open(page, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(html, 'lxml')
    a_tag_list = soup.findAll(name='a', attrs={'class', 'title'})
    all_title_link = []

    for a in a_tag_list:
        link = 'https:' + a.get('href')
        title = a.get('title')
        item = {'path': title, 'url': link}
        all_title_link.append(item)
    return all_title_link

def get_video_num(url):
    browser = webdriver.Firefox()
    browser.get(url)
    sleep(3)
    content = browser.find_elements_by_class_name('cur-page')[0].text
    # print(content)
    browser.quit()
    return content
def split_video_num(num):
    video_num=num.split('/')[1]
    return video_num
def ass_dict(page='222.html'):
    path_url_list=get_all_link(page)
    print(path_url_list)
    path_url_num=[]
    for item in path_url_list:
        print(item)
        url=item['url']
        print(url)
        all_num=get_video_num(url)
        real_num=split_video_num(all_num)
        item['num']=real_num
        print(item)
        path_url_num.append(item)
    print(path_url_num)


if __name__ == '__main__':
    ass_dict()
