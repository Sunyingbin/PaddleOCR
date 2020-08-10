import cv2
import numpy as np

image_name = '20200706140414.jpg'
image = cv2.imread(image_name)
print(image)

con = np.array(([[308, 588], [745, 601], [740, 733], [303, 720]]))

tmp = cv2.drawContours(image, [con], 0, (0, 0, 255), 3)

cv2.imshow('tmp', tmp)
cv2.waitKey(0)
cv2.destroyAllWindows()