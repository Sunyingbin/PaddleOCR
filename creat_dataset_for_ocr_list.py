import os
import json

url = 'C:\\Users\\18505\\Desktop\\电表\\output_meter'

trainTxt = url+'//train.txt'
trainFile = open(trainTxt, 'w')
testTxt = url+'//test.txt'
testFile = open(testTxt, 'w')

trainUrl = url+'//train'

for j in os.listdir(trainUrl):

    imgUrl = 'train/'+str(j)
    print(imgUrl)
    content = imgUrl +'\t'
    print(content)
    trainFile.write(content.replace("'", '"')+'\n')

trainFile.close()

#-----------------------------------------------------------------------------------------------------------------------

testUrl = url+'//test'

for j in os.listdir(testUrl):

    imgUrl = 'test/'+str(j)
    print(imgUrl)
    content = imgUrl +'\t'
    print(content)
    testFile.write(content.replace("'", '"')+'\n')

testFile.close()