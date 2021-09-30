# 暂停程序运行
import time
# 后面扒下来的数据是字符串里面包着字典，毫无可读性，可以通过json字符串和python字典的相互转换来提高可读性
import json
from browsermobproxy import Server
from selenium import webdriver
# 配置代理用
from selenium.webdriver.chrome.options import Options
import requests
import re

server = Server(r'C:\Program Files\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
server.start()
proxy = server.create_proxy()

chrome_options=Options()
print(proxy.proxy)
chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

driver = webdriver.Chrome('D:\Code\pythonProject\chromedriver.exe', options=chrome_options)
proxy.new_har("bili", options={'captureHeaders': True, 'captureContent': True})
video_url='https://www.bilibili.com/video/BV16q4y1o7EG?p=6'
driver.get(video_url)
time.sleep(5)

result = proxy.har
url=re.findall(r'https://i0.hdslb.com/bfs/subtitle/.+?json',str(result))
print(url)
# result_list=result['log']['entries'][116]['request']['url']
# print(result_list)
# print(result['log']['entries'][0])
# result_str=str(result)
# subtitle_urls = re.findall(r"subtitle_url\":\"(.*?json)", result_str)
# print(subtitle_urls)
# for url in subtitle_urls:
#     url = url.replace("\\u002F", "/")
#     print(url)
#     url_split_list=url.split('.')[-2].split('/')[-1]
#     print(url_split_list)


# with open('test.json','w',encoding='utf-8') as f:
#     f.write(json.dumps(result))
#     print('ok')

driver.quit()