import os
import json

url = 'C:\\Users\\18505\\Desktop\\电表\\yejing\\images'

trainTxt = url+'//train.txt'
trainFile = open(trainTxt, 'w')
testTxt = url+'//test.txt'
testFile = open(testTxt, 'w')

trainUrl = url+'//train'

for j in os.listdir(trainUrl):
    if j.find('.json') != -1:
        with open(trainUrl+'//'+j)as fp:
            json_data = json.load(fp)
            shapes = json_data['shapes']
            transcriptionList = []
            for shape in shapes:
                points = shape['points']
                list_to_int = []
                for each in points:
                    each_line = list(map(int, each))
                    list_to_int.append(each_line)
                # print(list_to_int)
                obj = {
                    "transcription": "111",
                    "points":list_to_int
                }
                transcriptionList.append(obj)

            imgUrl = 'train/' + str(j.split('.json')[0]) + '.jpg'
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
            shapes = json_data['shapes']
            transcriptionList = []
            for shape in shapes:

                points = shape['points']
                list_to_int = []
                for each in points:
                    each_line = list(map(int, each))
                    list_to_int.append(each_line)
                # print(list_to_int)

                obj = {
                    "transcription": "111",
                    "points":list_to_int
                }
                transcriptionList.append(obj)

            imgUrl = 'test/' + str(j.split('.json')[0]) + '.jpg'
            content = imgUrl +'\t'+str(transcriptionList)
            print(content)
            testFile.write(content.replace("'", '"')+'\n')

testFile.close()