from json import dumps
lost_video={'name':1,'num':2}
filename = 'lost_video.txt'
with open(filename, 'a') as file_object:
    lost_video_json=dumps(lost_video)
    file_object.write(lost_video_json+'\n')