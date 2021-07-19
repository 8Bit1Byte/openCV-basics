import cv2
import numpy as np
'''
WRAP PERSPECTIVE : USED FOR GET BIRD VIEW OF IMAGE(SEE FROM ABOVE)
'''
img = cv2.imread('./resources/photos/credit_cards.jpg')

width, height = 300, 130
pts_1 = np.float32([[196, 123], [532, 280], [407, 463], [67, 293]])
pts_2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

pers_transform = cv2.getPerspectiveTransform(pts_1, pts_2)
img_wrap = cv2.warpPerspective(img, pers_transform, (width, height))

cv2.imshow('Image', img)
cv2.imshow('Wrap Perspective', img_wrap)
cv2.waitKey(0)