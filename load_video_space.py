import os
from time import sleep
from selenium import webdriver


def get_video_id_one_page(page_url):
    browser = webdriver.Firefox()
    browser.get(page_url)
    sleep(3)
    content = browser.find_elements_by_tag_name('li')
    video_id_list = []
    for item in content:
        id = item.get_attribute('data-aid')
        if id:
            video_id_list.append(id)
    browser.quit()
    return video_id_list


def get_all_video_id(space_url, pages_num=1):
    all_url_in_space = [space_url + '?page=' + str(page_num) for page_num in range(1, pages_num + 1)]
    all_video_id = []
    for url in all_url_in_space:
        video_id_in_page = get_video_id_one_page(url)
        # print(video_id_in_page)
        all_video_id.extend(video_id_in_page)
    all_video_id = list(set(all_video_id))
    return all_video_id


def load_video_in_list(all_video_id, output, base_url='https://www.bilibili.com/video/'):
    for video_id in all_video_id:
        cmd = "you-get -o " + output + " " + base_url + video_id
        os.system(cmd)


if __name__ == '__main__':
    space_url = 'https://space.bilibili.com/349060406/video'
    pages_num = 1
    ouput_path = "D:\Video\亢少军的课程"
    all_video_id = get_all_video_id(space_url, pages_num)
    load_video_in_list(all_video_id, ouput_path)
