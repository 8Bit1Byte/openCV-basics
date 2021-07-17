'''
Process Android phone live stream using OpenCV and Python
https://www.youtube.com/watch?v=-mJXEzSD1Ic
Just install :

1> Ip Webcame on Phone
2> Go to http://192.168.0.100:8080/ on browser
'''

import numpy as np
import cv2
import requests

url = 'http://192.168.0.100:8080/photo.jpg'

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    cv2.imshow('Android CAM', img)

    if cv2.waitKey(1) & 0xFF  == ord('q'):
        break    