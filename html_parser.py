import os
from json import dumps
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_all_link(page):
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
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    sleep(3)
    content = browser.find_elements_by_class_name('cur-page')[0].text
    # print(content)
    browser.quit()
    return content


def split_video_num(num):
    video_num = num.split('/')[1]
    return video_num


def ass_dict(page):
    path_url_list = get_all_link(page)
    print(path_url_list)
    path_url_num_list = []
    for item in path_url_list:
        print(item)
        url = item['url']
        print(url)
        all_num = get_video_num(url)
        real_num = split_video_num(all_num)
        item['num'] = real_num
        print(item)
        path_url_num_list.append(item)
        print('新的path_url_num：\n')
        print(path_url_num_list)
    return path_url_num_list


def download_one_video(path, url):
    try:
        command_word = "you-get -o " + path + " " + url
        os.system(command_word)
    except:
        lost_video = {'vidio_name': path, 'video_url': url}
        filename = 'lost_video.txt'
        with open(filename, 'a') as file_object:
            lost_video_json = dumps(lost_video)
            file_object.write(lost_video_json + '\n')


def download_playlist_video(path_url_num_list, base_path):
    for item in path_url_num_list:
        path = base_path + item['path']
        url = item['url']
        num = item['num']
        print(path)
        for video_num in range(int(num)):
            video_url = url + '?p=' + str(video_num + 1)
            print(video_url)
            download_one_video(path, video_url)


if __name__ == '__main__':
    page='111.html'
    base_path='D:\Video\西方哲学专题讲座\\'
    path_url_num_list=ass_dict(page)
    download_playlist_video(path_url_num_list,base_path)
    path_url_num_list = [
        # {'path': '【西方哲学十四.1】唯物史观-马克思', 'url': 'https://www.bilibili.com/video/BV1Ki4y1b7G4', 'num': '11'},
        # {'path': '【西方哲学六.4】思考绵延-柏格森', 'url': 'https://www.bilibili.com/video/BV1Uk4y1r7zP', 'num': '11'},
        # {'path': '【西方哲学六.3】那个个体-克尔凯郭尔', 'url': 'https://www.bilibili.com/video/BV1tK4y1b7aV', 'num': '10'},
        # {'path': '【西方哲学七.7】时间与叙述-利科', 'url': 'https://www.bilibili.com/video/BV1GZ4y1474h', 'num': '9'},
        # {'path': '【西方哲学七.6】视域融合-伽达默尔', 'url': 'https://www.bilibili.com/video/BV1XQ4y1K7i3', 'num': '10'},
        # {'path': '【西方哲学七.5】知觉世界-梅洛庞蒂', 'url': 'https://www.bilibili.com/video/BV1RT4y137JR', 'num': '7'},
        # {'path': '【西方哲学七.4】为他存有-列维纳斯', 'url': 'https://www.bilibili.com/video/BV1Ba4y1t7ZA', 'num': '8'},
        # {'path': '【西方哲学十三.3】解构主义-德里达', 'url': 'https://www.bilibili.com/video/BV1kE411F7xk', 'num': '9'},
        # {'path': '【西方哲学十三.1】镜像三界-拉康', 'url': 'https://www.bilibili.com/video/BV12E411M75s', 'num': '26'},
        # {'path': '【西方哲学十二.3】结构主义人类学-列维斯特劳斯', 'url': 'https://www.bilibili.com/video/BV1PE411n7m6', 'num': '9'},
        # {'path': '【西方哲学十二.2】精神分析-弗洛伊德', 'url': 'https://www.bilibili.com/video/BV17j411f7mf', 'num': '10'},
        # {'path': '【西方哲学十二.1】结构主义语言学-索绪尔', 'url': 'https://www.bilibili.com/video/BV1s7411n7jk', 'num': '10'},
        # {'path': '【西方哲学十一.3】科学研究纲领-拉卡托斯', 'url': 'https://www.bilibili.com/video/BV1w7411b7wf', 'num': '5'},
        # {'path': '【西方哲学十一.2】范式转移-库恩', 'url': 'https://www.bilibili.com/video/BV1b7411W7qg', 'num': '8'},
        # {'path': '【西方哲学十一.1】证伪主义-波普尔', 'url': 'https://www.bilibili.com/video/BV1b7411k7Bg', 'num': '10'},
        # {'path': '【西方哲学十.3】逻辑实用主义-奎因', 'url': 'https://www.bilibili.com/video/BV1X7411v7z9', 'num': '11'},
        # {'path': '【西方哲学十.2】日常语言学派-牛津学派', 'url': 'https://www.bilibili.com/video/BV1RJ41157h4', 'num': '11'},
        # {'path': '【西方哲学十.1】逻辑实证主义-维也纳学派', 'url': 'https://www.bilibili.com/video/BV1nJ411e7bV', 'num': '11'},
        # {'path': '【西方哲学九.3】语言游戏-维特根斯坦', 'url': 'https://www.bilibili.com/video/BV1MJ411479n', 'num': '14'},
        # {'path': '【西方哲学九.2】摹状词理论-罗素', 'url': 'https://www.bilibili.com/video/BV1nJ411k7JH', 'num': '6'},
        # {'path': '【西方哲学九.1】数理逻辑-弗雷格', 'url': 'https://www.bilibili.com/video/BV15J411v7hf', 'num': '5'},
        # {'path': '【西方哲学八.3】实用主义-杜威', 'url': 'https://www.bilibili.com/video/BV1jJ411z7Jx', 'num': '11'},
        # {'path': '【西方哲学八.2】彻底经验主义-詹姆斯', 'url': 'https://www.bilibili.com/video/BV1BJ411973c', 'num': '12'},
        # {'path': '【西方哲学八.1】意义就是效果-皮尔士', 'url': 'https://www.bilibili.com/video/BV1SJ41127zS', 'num': '12'},
        {'path': '【西方哲学七.3】存在主义-萨特', 'url': 'https://www.bilibili.com/video/BV1uE411i7cc', 'num': '6'},
        {'path': '【西方哲学七.2】向死而在-海德格尔', 'url': 'https://www.bilibili.com/video/BV1zE411q7HC', 'num': '16'},
        {'path': '【西方哲学七.1】现象学-胡塞尔', 'url': 'https://www.bilibili.com/video/BV1PE411h7m4', 'num': '22'},
        {'path': '【西方哲学五.4】绝对精神-黑格尔', 'url': 'https://www.bilibili.com/video/BV1pE41167g7', 'num': '31'},
        {'path': '【西方哲学六.1】意志主义-叔本华', 'url': 'https://www.bilibili.com/video/BV1ME411y7Nu', 'num': '11'},
        {'path': '【西方哲学六.2】上帝已死-尼采', 'url': 'https://www.bilibili.com/video/BV1kE411C7cS', 'num': '10'},
        {'path': '【西方哲学五.3】绝对理性-谢林', 'url': 'https://www.bilibili.com/video/BV1UE41197gG', 'num': '4'},
        {'path': '【西方哲学五.2】知识学-费希特', 'url': 'https://www.bilibili.com/video/BV1rJ411g7KH', 'num': '7'},
        {'path': '【西方哲学五.1】三大批判-康德', 'url': 'https://www.bilibili.com/video/BV18J411c7XX', 'num': '30'},
        {'path': '【西方哲学四.3】怀疑论-休谟', 'url': 'https://www.bilibili.com/video/BV1c4411y7Ez', 'num': '6'},
        {'path': '【西方哲学四.2】存在即被感知-贝克莱', 'url': 'https://www.bilibili.com/video/BV1N4411z7Sq', 'num': '5'},
        {'path': '【西方哲学四.1】白板说-洛克', 'url': 'https://www.bilibili.com/video/BV1k4411B7RD', 'num': '6'},
        {'path': '【西方哲学三.3】单子论-莱布尼茨', 'url': 'https://www.bilibili.com/video/BV1j44116764', 'num': '4'},
        {'path': '【西方哲学三.2】自然神论-斯宾诺莎', 'url': 'https://www.bilibili.com/video/BV1s4411k7TN', 'num': '6'},
        {'path': '【西方哲学三.1】我思故我在-笛卡尔', 'url': 'https://www.bilibili.com/video/BV1o4411r7o5', 'num': '5'},
        {'path': '【西方哲学二.2】经院哲学-托马斯·阿奎纳', 'url': 'https://www.bilibili.com/video/BV1B4411r7n1', 'num': '3'},
        {'path': '【西方哲学二.1】上帝之城-奥古斯丁', 'url': 'https://www.bilibili.com/video/BV1i4411r7ih', 'num': '8'},
        {'path': '【西方哲学一.3】形而上学-亚里士多德', 'url': 'https://www.bilibili.com/video/BV1G4411r7Gr', 'num': '6'},
        {'path': '【西方哲学一.2】理念世界—柏拉图', 'url': 'https://www.bilibili.com/video/BV1W4411R7DC', 'num': '8'},
        {'path': '【西方哲学一.1】认识你自己—苏格拉底', 'url': 'https://www.bilibili.com/video/BV1G4411R7bA', 'num': '6'},
        {'path': '【西方哲学】 分支哲学的简单认识', 'url': 'https://www.bilibili.com/video/BV1C441197hE', 'num': '11'},
        {'path': '【西方哲学】  元哲学的基本认识', 'url': 'https://www.bilibili.com/video/BV1r4411975S', 'num': '8'},
        {'path': '【西方哲学】西方哲学史与二元对立心态', 'url': 'https://www.bilibili.com/video/BV1z441197aH', 'num': '7'},
        {'path': '先秦诸子思想概论', 'url': 'https://www.bilibili.com/video/BV1V441197wh', 'num': '8'}]
    # for item in path_url_num_list:
    #     path = 'D:\Video\西方哲学专题讲座\\' + item['path']
    #     url = item['url']
    #     num = item['num']
    #     print(path)
    #     for i in range(int(num)):
    #         video_url = url + '?p=' + str(i + 1)
    #         print(video_url)
    #         download_one_video(path, video_url)
