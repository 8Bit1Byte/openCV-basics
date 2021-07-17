'''
Read and Show
1. Image
2. Video
3. Webcam
'''

import cv2

''' 
IMAGES READ AND SHOW OPERATION
'''
def imageOper():    
    # 1. Read an image [cv2.imread]
    img = cv2.imread('./resources/Photos/Lamborghin-blue.webp')

    cv2.imshow('Hello Image', img)
    # 1. waitKey(0) will display the window infinitely until any keypress (it is suitable for image display). 
    # 2. waitKey(1) will display a frame for 1 ms, after which display will be automatically closed.
    cv2.waitKey(0)

''' 
VIDEO READ AND SHOW OPERATION
'''
def videoOper():    
    # 1. Cature a Video [cv2.VideoCapture]
    # 2. About videocapture object https://www.geeksforgeeks.org/how-to-get-properties-of-python-cv2-videocapture-object/
    vidCap = cv2.VideoCapture('./resources/videos/dog.mp4')
    while True:
        success, img = vidCap.read()
        if (cv2.waitKey(1) & 0xFF == ord('q')) or not success:
            break
        cv2.imshow('Hello Video', img)

''' 
WEBCAM READ AND SHOW OPERATION
'''
def webCamOper():    
    # 1. Cature a WebCam [cv2.VideoCapture]
    # 2. About videocapture object https://www.geeksforgeeks.org/how-to-get-properties-of-python-cv2-videocapture-object/
    # 3. Webcam and Video play is similar just we need to pass the id of Camera
    camCap = cv2.VideoCapture(0)
    # define parameter for this object using [cv2.set(id, value)]
    camCap.set(3, 640)
    camCap.set(4, 480)
    camCap.set(10, 100)
    while True:
        success, img = camCap.read()
        if (cv2.waitKey(100) & 0xFF == ord('q')) or not success:
            break
        cv2.imshow('Hello Video', img)

if __name__ == '__main__':
    choices = {
        1: imageOper,
        2: videoOper,
        3: webCamOper
    }
    choice = int(input('Enter your choice : '))
    opern = choices[choice]
    opern()