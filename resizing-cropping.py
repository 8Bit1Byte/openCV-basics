import cv2
from numpy.core.fromnumeric import choose

img_rgb = cv2.imread('./resources/photos/bugatti-small.jpg')

'''
FOR RESIZING [cv2.resize]
'''
img_resize = cv2.resize(img_rgb, (300, 200))
'''
FOR CROPPING [use basic numpy subarray accessing property]
'''
img_crop = img_rgb[:, 150:400]
'''
height = img.shape[0]
FOR DYNAMIC IMAGE RESIZE AUTOMATICLLY
while height/2 > 1:
    height /= 1.01
    img_resize = cv2.resize(img, (300, int(height)))
    if cv2.waitKey(34) & 0xFF == ord(chr(27)):
        break
    cv2.imshow('Resized Image', img_resize)
'''


if __name__ == '__main__':
    choices = {
        1: img_resize,
        2: None
    }
    choice = int(input('Enter your operation code : '))
    img = choices[choice]
    if choice == 1:
        cv2.imshow('Resized Image', img)
    if choice == 2:
        cv2.imshow('Cropped Image', img_crop)
    cv2.waitKey(0)