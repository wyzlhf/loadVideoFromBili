import requests
import subprocess


def get_page_json(spaceID: int, page_num: int) -> list:
    base_space_search_url = 'https://api.bilibili.com/x/space/arc/search?mid='
    bvid_list = []
    for page in range(page_num):
        # print(page+1)
        space_page_url = base_space_search_url + str(spaceID) + '&pn=' + str(page + 1)
        space_page_json = requests.get(space_page_url).json()
        vlist = space_page_json["data"]["list"]["vlist"]
        for v in vlist:
            bvid_list.append(v["bvid"])
    return bvid_list


def load_space_video(spaceID: int, page_num: int) -> None:
    bvid_list = get_page_json(spaceID, page_num)
    # bvid_list =get_person_space(spaceID,page_num)
    for bvid in bvid_list:
        video_url = 'https://www.bilibili.com/video/' + bvid
        subprocess.Popen([
            'you-get',
            video_url
        ]).communicate()


def get_person_space(spaceID: int, page_num: int, series_id: int) -> list:
    print("程序开始执行，开始获取个人空间bvid……")
    bvid_list = []
    for page in range(page_num):
        get_json_url = f'https://api.bilibili.com/x/series/archives?mid={spaceID}&series_id={series_id}&only_normal=true&sort=desc&pn={page + 1}&ps=30'
        person_space_json = requests.get(get_json_url).json()
        vlist = person_space_json["data"]["archives"]
        for item in vlist:
            bvid_list.append(item["bvid"])
    print("获取到个人空间所有视频bvid成功，请稍后，开始对视频进行逐个下载……")
    return bvid_list


def load_person_space_video(spaceID: int, page_num: int, series_id: int) -> None:
    # bvid_list = get_page_json(spaceID, page_num)
    bvid_list =get_person_space(spaceID,page_num, series_id)
    for bvid in bvid_list:
        print('----------------------------------------------------------------')
        print(f'正在下载第{bvid_list.index(bvid)+1}个视频，请耐心等待……')
        video_url = 'https://www.bilibili.com/video/' + bvid
        try:
            subprocess.Popen([
                'you-get',
                video_url
            ]).communicate()
        except Exception as e:
            print('发生异常，视频下载失败……')
            print(bvid)
        else:
            print(f'第{bvid_list.index(bvid)+1}个视频下载完成。总视频个数为{len(bvid_list)}')
            # print('----------------------------------------------------------------')


if __name__ == '__main__':
    # load_space_video(483162496,10)
    # bvid_list=
    load_person_space_video(483162496, 1,292495)
