import os
import json

url = 'C:\\Users\\18505\\Desktop\\电表\\jixiezilun'

trainTxt = url+'//train.txt'
trainFile = open(trainTxt, 'w')
testTxt = url+'//test.txt'
testFile = open(testTxt, 'w')

trainUrl = url+'//train'

for j in os.listdir(trainUrl):
    if j.find('.json') != -1:
        with open(trainUrl+'//'+j)as fp:
            json_data = json.load(fp)
            points = json_data['shapes'][0]['points']
            list_to_int = []
            for each in points:
                each_line = list(map(int, each))
                list_to_int.append(each_line)
            # print(list_to_int)
            transcriptionList = []
            obj = {
                "transcription": "000",
                "points":list_to_int
            }
            transcriptionList.append(obj)
            imgUrl = 'train/'+str(j.split('.json')[0])+'.jpg'
            print(imgUrl)
            content = imgUrl +'\t'+str(transcriptionList)
            print(content)
            trainFile.write(content.replace("'", '"')+'\n')

trainFile.close()

#-----------------------------------------------------------------------------------------------------------------------

testUrl = url+'//test'

for j in os.listdir(testUrl):
    if j.find('.json') != -1:
        with open(testUrl+'//'+j)as fp:
            json_data = json.load(fp)
            points = json_data['shapes'][0]['points']
            list_to_int = []
            for each in points:
                each_line = list(map(int, each))
                list_to_int.append(each_line)
            # print(list_to_int)
            transcriptionList = []
            obj = {
                "transcription": "000",
                "points":list_to_int
            }
            transcriptionList.append(obj)
            imgUrl = 'test/'+str(j.split('.json')[0])+'.jpg'
            print(imgUrl)
            content = imgUrl +'\t'+str(transcriptionList)
            print(content)
            testFile.write(content.replace("'", '"')+'\n')

testFile.close()