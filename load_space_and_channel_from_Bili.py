import subprocess

import requests


# Space视频页面链接：https://space.bilibili.com/170920967/video
# Channel页面链接：https://space.bilibili.com/170920967/channel/collectiondetail?sid=42926，多了sid

# Space json链接:https://api.bilibili.com/x/space/arc/search?mid=170920967&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp
# Channel json链接：https://api.bilibili.com/x/polymer/space/seasons_archives_list?mid=170920967&season_id=42926&sort_reverse=false&page_num=1&page_size=30

def get_page_num(total_video:int,video_num_per_page:int=30)->int:
    print('正在获取空间/频道总页数。。。')
    div:int=total_video//video_num_per_page
    mod:int=total_video%video_num_per_page
    page_num:int
    if mod==0:
        page_num=div
        return page_num
    else:
        page_num=div+1
        return page_num

def get_json(json_url:str)->dict:
    url_json:dict=requests.get(json_url).json()
    # print(url_json)
    return url_json

def get_count_ps(mid:int,season_id:int=None)->(int,int):
    if season_id:
        #此处为channel
        channel_url=f'https://api.bilibili.com/x/polymer/space/seasons_archives_list?mid={mid}&season_id={season_id}&page_num=1&page_size=30'
        fist_page_json:dict=get_json(channel_url)
        data_page:dict=fist_page_json['data']['page']
        page_size:int=int(data_page['page_size'])
        total:int=int(data_page['total'])
        return (page_size,total)
    else:
        space_url=f'https://api.bilibili.com/x/space/arc/search?mid={mid}'
        fist_page_json:dict = get_json(space_url)
        data_page: dict = fist_page_json['data']['page']
        ps:int=int(data_page['ps'])
        count:int=int(data_page['count'])
        return (ps,count)

def get_space_or_channel_list(mid:int,season_id:int=None)->list:
    page_size,total=get_count_ps(mid,season_id)
    page_num:int=get_page_num(total,page_size)
    # print(page_num)
    bv_list:list=[]
    if season_id: #这是一个channel
        for page in range(page_num):
            channle_url=f'https://api.bilibili.com/x/polymer/space/seasons_archives_list?mid={mid}&season_id={season_id}&page_num={page+1}&page_size=30'
            page_json: dict = get_json(channle_url)
            archives:list=page_json['data']['archives']
            for item in archives:
                bvid:str=item['bvid']
                bv_list.append(bvid)
        return bv_list

            # bv_num=
    else: #这是一个space
        for page in range(page_num):
            space_url=f'https://api.bilibili.com/x/space/arc/search?mid={mid}&pn={page+1}'
            page_json:dict = get_json(space_url)
            vlist:list=page_json['data']['list']['vlist']
            for item in vlist:
                bvid:str=item['bvid']
                bv_list.append(bvid)
        return bv_list

def load_every_video(mid:int,season_id:int=None)->None:
    print('开始下载，请稍后。。。')
    bv_list=get_space_or_channel_list(mid,season_id)
    for bvid in bv_list:
        print('----------------------------------------------------------------')
        print(f'正在下载第{bv_list.index(bvid) + 1}/{len(bv_list)}个视频，请耐心等待……')
        video_url = 'https://www.bilibili.com/video/' + bvid
        subprocess.Popen([
            'you-get',
            video_url
        ]).communicate()


if __name__ == '__main__':
    load_every_video(
        170920967,
        42926
    )
