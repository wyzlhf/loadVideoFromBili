import requests
import json
import os


class ChannelVideos(object):
    def __init__(self, page_number,
                 base_url,
                 out_path='',
                 channel_url='https://api.bilibili.com/x/space/channel/video?mid=394612055&cid=200461&pn='):
        self.page_number = page_number
        self.base_url=base_url
        self.channel_url = channel_url
        self.out_path = out_path
        self.load_videos()

    def get_channel_urls(self):
        channel_urls = []
        for num in range(self.page_number):
            channel_url = self.channel_url + str(num + 1)
            channel_urls.append(channel_url)
        return channel_urls

    def get_page_bvid(self, url):
        bvid_list = []
        channel_json = requests.get(url).text
        json_data = json.loads(channel_json)
        bvid_json_list = json_data['data']['list']['archives']
        for item in bvid_json_list:
            bvid = item['bvid']
            bvid_list.append(bvid)
        return bvid_list

    def get_all_bvids(self):
        all_bvid_list = []
        channel_pages = self.get_channel_urls()
        for url in channel_pages:
            page_bvid_list = self.get_page_bvid(url)
            all_bvid_list.extend(page_bvid_list)
        return all_bvid_list

    def load_videos(self):
        all_bvid_list = self.get_all_bvids()
        for bvid in all_bvid_list:
            video_url = self.base_url + bvid
            command_word = "you-get -o " + self.out_path + " " + video_url
            os.system(command_word)


if __name__ == '__main__':
    # channel_videos=ChannelVideos(3)
    # all_bvid_list=channel_videos.get_all_bvids()
    # print(all_bvid_list)
    #
    # channel_videos = ChannelVideos(3)
    # all_bvid_list = channel_videos.get_all_bvids()
    base_url = 'https://www.bilibili.com/video/'
    # out_put_path = r"D:\Video\WebRTC视频教程-H5"
    # for bvid in all_bvid_list:
    #     url = base_url + bvid
    #     command_word = "you-get -o " + out_put_path + " " + url
    #     os.system(command_word)
    page_number=3
    out_path=r'D:\Video\test'
    channelVideos=ChannelVideos(page_number,base_url,out_path)
