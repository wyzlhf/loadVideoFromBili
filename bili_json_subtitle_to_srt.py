import json

def ms_to_hours(millis):

    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24
    hours = int(hours)
    lay = millis - hours*1000 * 60 * 60 - minutes*1000 * 60 - seconds*1000

    return("%d:%d:%d.%d" % (hours, minutes, seconds,lay))

def convert_subtitle(fileDir:str='subtitle.json')->None:
    contentBody:list= []
    with open(fileDir,'r',encoding='utf8') as file:
        jsonContent:str=file.read()
        dictContent:dict=json.loads(jsonContent)
        contentBody=dictContent['body']

    srtDir =fileDir.split('.')[0]+'.srt'
    for item in contentBody:
        fromTime:float=item['from']
        intFromMS:int=int(fromTime*1000)
        startTime:str=ms_to_hours(intFromMS).replace('.',',')

        toTime:float=item['to']
        intToMS:int=int(toTime*1000)
        endTime:str=ms_to_hours(intToMS).replace('.',',')

        content:str=item['content']
        index=contentBody.index(item)+1
        formedTime=startTime+'-->'+endTime

        with open(srtDir,'a',encoding='utf-8') as srt:
            srt.write(str(index)+'\n')
            srt.write(formedTime+'\n')
            srt.write(content+'\n')




if __name__ == '__main__':
    # print(strftime("%H:%M:%S", gmtime(172.90)))
    # print(ms_to_hours(720))
    convert_subtitle()