import json

import requests
from requests import Response


# from requests.api import


class LoadPlaylistSubtitle(object):
    '''
    字幕json格式链接：https://i0.hdslb.com/bfs/subtitle/b3eaf7b000edc13a0ff94b7335201fe9e01b61fe.json
    https://api.bilibili.com/x/player/v2?cid=542890058&aid=467084764&bvid=BV1KL411K7cH   需要cid，aid，bivid，

    然后，https://api.bilibili.com/x/player/pagelist?bvid=BV1KL411K7cH&jsonp=jsonp   里面有cid
    ###https://api.bilibili.com/x/player/pagelist?bvid=BV1KL411K7cH&jsonp=jsonp     这里可以获取playlist的所有cid



    https://api.bilibili.com/x/web-interface/view/detail?bvid=BV1KL411K7cH&aid=467084764&need_operation_card=1
    &web_rm_repeat=1&need_elec=1&out_referer=https%3A%2F%2Fwww.bilibili.com%2F

    此处可以获取整个包括playlist的该页面总览信息，其中包括推荐列表

    目前是使用手动也就是人肉的方式判断是否有字幕，如果改进可以加上自动判断是否存在字幕的逻辑

    '''

    def __init__(self, BVID: str):
        print('开始下载json文件，程序较大，请耐心等候。。。')
        print('---------------------------------------------')
        self.BVID = BVID
        self.headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                          '88.0.4324.150 Safari/537.36 Edg/88.0.705.63'}

    def get_video_info(self) -> (int, list):
        detail_url: str = 'https://api.bilibili.com/x/web-interface/view/detail?bvid=' + self.BVID
        # headers: dict = {
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        #                   '88.0.4324.150 Safari/537.36 Edg/88.0.705.63'}
        playlist_info_res: Response = requests.get(detail_url, headers=self.headers)
        playlist_info_str: str = playlist_info_res.text
        playlist_info_dict: dict = json.loads(playlist_info_str)
        aid: int = playlist_info_dict["data"]["View"]["aid"]

        pages: list = playlist_info_dict["data"]["View"]["pages"]

        # print(pages)

        cid_part_order_list: list = []

        for item in pages:
            cid:int=item['cid']
            part=item['part']
            # print(part)
            part_dict:dict={'cid':cid,'part':part,'order':pages.index(item)+1}
            cid_part_order_list.append(part_dict)
        # print(cid_list)
        return (aid, cid_part_order_list)

    def get_json_url(self):
        aid, cid_part_order_list = self.get_video_info()

        for cid_part_order_dict in cid_part_order_list:
            cid=cid_part_order_dict['cid']
            player_url:str=f'https://api.bilibili.com/x/player/v2?cid={cid}&aid={aid}&bvid={self.BVID}'
            player_content:Response=requests.get(player_url,headers=self.headers)
            content_str:str=player_content.text
            content_dict:dict=json.loads(content_str)
            subtitle_url:str=content_dict['data']['subtitle']['subtitles'][0]['subtitle_url']
            subtitle_url='https:'+subtitle_url

            json_content_dict:dict=requests.get(subtitle_url).json()
            json_content_str:str=json.dumps(json_content_dict)
            # print(type(json_content_str))
            with open(cid_part_order_dict['part']+'.json','a') as json_file:
                print('正在写入json文件：',cid_part_order_dict['part'])
                json_file.write(json_content_str)
                print(f'第{cid_part_order_list.index(cid_part_order_dict)}/{len(cid_part_order_list)}个字幕文件下载完成')
                print('---------------------------------------------')





if __name__ == '__main__':
    s = LoadPlaylistSubtitle('BV1KL411K7cH')
    s.get_json_url()
