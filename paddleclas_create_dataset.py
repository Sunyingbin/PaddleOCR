import os
import json


url = 'C:\\Users\\18505\\Desktop\\电表\\PaddleClas\\meterClas'

trainTxt = url+'//train_list.txt'
trainFile = open(trainTxt, 'w')
valTxt = url+'//val_list.txt'
valFile = open(valTxt, 'w')

trainUrl1 = url+'//water//train'
trainUrl2 = url+'//yejing//train'

for j in os.listdir(trainUrl1):

    imgUrl = 'water/train/'+str(j)
    print(imgUrl)
    content = imgUrl+' '+'0' +'\t'
    print(content)
    trainFile.write(content.replace("'", '"')+'\n')

for j in os.listdir(trainUrl2):

    imgUrl = 'yejing/train/'+str(j)
    print(imgUrl)
    content = imgUrl+' '+'1' +'\t'
    print(content)
    trainFile.write(content.replace("'", '"')+'\n')

trainFile.close()



valUrl1 = url+'//water//val'
valUrl2 = url+'//yejing//val'

for j in os.listdir(valUrl1):

    imgUrl = 'water/val/'+str(j)
    print(imgUrl)
    content = imgUrl+' '+'0' +'\t'
    print(content)
    valFile.write(content.replace("'", '"')+'\n')

for j in os.listdir(valUrl2):

    imgUrl = 'yejing/val/'+str(j)
    print(imgUrl)
    content = imgUrl+' '+'1' +'\t'
    print(content)
    valFile.write(content.replace("'", '"')+'\n')

valFile.close()

