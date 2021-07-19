import cv2
import numpy as np
'''
MULTIPLE IMAGE ON SAME WINDOW : SUBPLOT[IN MATPLOTLIB]
'''

'''
Simplest is to go with [numpy.hstack | numpy.vstack]
ISSUES:
1. Images may have different channels(color spaces)
2. May different sizes
3. Resize image issue and when stacking it may cross the main screen
'''

img_1 = cv2.imread('./resources/photos/bugatti-small.jpg')
img_2 = cv2.imread('./resources/photos/bugatti-small.jpg')
img = np.hstack((img_1, img_2))
img = np.vstack((img_1, img_2))

# shp = img.shape[:-1]
# if shp[1] > 1024 or shp[0] > 720:
#     diff = shp[1] - 1024
#     img = cv2.resize(img, (shp[1]//10, shp[0]//10))

cv2.imshow('Stacked Image', img)
cv2.waitKey(0)