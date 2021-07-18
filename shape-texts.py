'''
CREATING SHAPE TEXT IN IMAGES
'''
import cv2
import numpy as np

img = cv2.imread('./resources/photos/bugatti-small.jpg')

'''
Shape using default functionlity 
Means by using numpy array
'''
def baisc_method():
    img_grey = np.full((512, 512), 100, dtype=np.uint8)
    cv2.imshow('Grey Blank Image', img_grey)
    img_grey[:, :200] = 0 
    cv2.imshow('Grey Blank Image', img_grey)
    cv2.waitKey(0)

'''
FOR DYANAMIC IMAGE
for i in range(256):    
    img_grey = np.full((512, 512), i, dtype=np.uint8)
    cv2.imshow('Grey Blank Image', img_grey)
    cv2.waitKey(1)
'''


'''
USING INBULIT FUNCTIONLITY OF OPENCV
'''

'''
FOR LINE [cv2.line]
'''
def line_on_image(img):    
    img_line = cv2.line(img, (0, 0), (300, 300), (255, 0, 0), thickness=1)
    cv2.imshow('Line on Image', img_line)
    cv2.waitKey(0)

def rect_on_image(img):    
    img_line = cv2.rectangle(img, (10,10), (300, 300), (255, 255, 0), thickness=cv2.FILLED)
    cv2.imshow('Rectangle on Image', img_line)
    cv2.waitKey(0)

def circle_on_image(img):    
    img_line = cv2.circle(img, (100, 100), 20, (255, 255, 0), thickness=cv2.FILLED)
    cv2.imshow('Circle on Image', img_line)
    cv2.waitKey(0)
'''
FOR DYNAMIC CIRCLE
for i in range(600):
    print(i, ' =>')
    if i < 150:
        img_line = cv2.circle(img, (200, 200), i, (255, 255, 0), thickness=cv2.FILLED)
    elif i > 150 and i < 300:
        img_line = cv2.circle(img, (200, 200), i//2, (0, 255, 0), thickness=cv2.FILLED)
    elif i > 300 and i < 450:
        img_line = cv2.circle(img, (200, 200), i//4, (0, 255, 255), thickness=cv2.FILLED)
    else:
        img_line = cv2.circle(img, (200, 200), i//8, (255, 0, 255), thickness=cv2.FILLED)
    cv2.imshow('Line on Image', img_line)
    cv2.waitKey(1)
'''

def text_on_image(img):    
    img_line = cv2.putText(img, 'Hello', (100, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), thickness=3)
    cv2.imshow('Text on Image', img_line)
    cv2.waitKey(0)

cv2.waitKey(0)
text_on_image(img)