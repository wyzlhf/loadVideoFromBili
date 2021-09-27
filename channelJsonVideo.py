import requests
import json

class ChannelVideos(object):
    def __init__(self,page_number,base_url='https://api.bilibili.com/x/space/channel/video?mid=394612055&cid=200461&pn='):
        self.page_number=page_number
        self.base_url=base_url
    def get_channel_urls(self):
        channel_urls=[]
        for num in range(self.page_number):
            channel_url=self.base_url+str(num+1)
            channel_urls.append(channel_url)
        return channel_urls
    def get_page_bvid(self,url):
        bvid_list=[]
        channel_json=requests.get(url).text
        json_data=json.loads(channel_json)
        bvid_json_list=json_data['data']['list']['archives']
        for item in bvid_json_list:
            bvid=item['bvid']
            bvid_list.append(bvid)
        return bvid_list
    def get_all_bvids(self):
        all_bvid_list=[]
        channel_pages=self.get_channel_urls()
        for url in channel_pages:
            page_bvid_list=self.get_page_bvid(url)
            all_bvid_list.extend(page_bvid_list)
        return all_bvid_list

if __name__ == '__main__':
    channel_videos=ChannelVideos(3)
    all_bvid_list=channel_videos.get_all_bvids()
    print(all_bvid_list)
