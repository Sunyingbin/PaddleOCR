




url = 'C:\\Users\\18505\\Desktop\\电表\\PaddleClas\\little_meter_new'

labelListTxt = url+'//label_list.txt'
listListFile = open(labelListTxt, 'w')

a = 0
b = 0

for num in range(0, 100):

    if b == 10:
        b = 0
        a = a + 1
    content = str(a) + str(b) +'\t'
    listListFile.write(content.replace("'", '"') + '\n')
    b = b + 1
    print(content)

listListFile.close()