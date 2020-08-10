import os
import json


url = 'C:\\Users\\18505\\Desktop\\电表\\PaddleClas\\little_meter_new'

trainTxt = url+'//train_list.txt'
trainFile = open(trainTxt, 'w')
valTxt = url+'//val_list.txt'
valFile = open(valTxt, 'w')

Labelurl = url+'//data_raw_all'

number = 0
aa = ['0']
for j in os.listdir(Labelurl):

    s = str(j).split('_')[0].replace('.','')
    if int(s) < 0.8 or int(s) > 9.7:
        s = '0'
    elif int(s) < 1.8:
        s = '1'
    elif int(s) < 2.8:
        s = '2'
    elif int(s) < 3.8:
        s = '3'
    elif int(s) < 4.8:
        s = '4'
    elif int(s) < 5.8:
        s = '5'
    elif int(s) < 6.8:
        s = '6'
    elif int(s) < 7.8:
        s = '7'
    elif int(s) < 8.8:
        s = '8'
    else:
        s = '9'

    print(s)

    imgUrl = 'data_raw_all/'+str(j)
    print(imgUrl)
    content = imgUrl+' '+ s +'\t'
    print(content)


    if aa[len(aa)-1] != s:
        valFile.write(content.replace("'", '"') + '\n')
        number = 0

    if number <= 4:
        valFile.write(content.replace("'", '"') + '\n')
        number = number + 1
    else:
        trainFile.write(content.replace("'", '"') + '\n')

    aa.append(s)
trainFile.close()
valFile.close()

