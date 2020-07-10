import cv2
import numpy as np

image_name = '20200525141721.png'
image = cv2.imread(image_name)
print(image)

con = np.array(([[315, 212], [547, 237], [540, 305], [308, 280]]))

tmp = cv2.drawContours(image, [con], 0, (0, 0, 255), 3)

cv2.imshow('tmp', tmp)
cv2.waitKey(0)
cv2.destroyAllWindows()