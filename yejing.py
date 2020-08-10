# coding: utf8
import requests
import json
import cv2
import base64
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tostring()).decode('utf8')

# 发送HTTP请求

data = {'images':[cv2_to_base64(cv2.imread("20200629172851.jpg"))]}
headers = {"Content-type": "application/json"}
url = "http://127.0.0.1:8866/predict/yejing_ocr_db_crnn_mobile"
r = requests.post(url=url, headers=headers, data=json.dumps(data))

# 图片展示
img = mpimg.imread("20200629172851.jpg")
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis('off')
plt.show()

# 打印预测结果
print(r.json())
print(r.json()["results"])

