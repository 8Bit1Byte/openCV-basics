import cv2

'''
cv2.imread : convert image into numpy array
cv2.cvtColor : convert color space (code argument)
cv2.GaussianBlur : kernal (7, 7) must be odd number
'''

# NOTE : A Kernel tells you how to change the value of any given 
#        pixel by combining it with different amounts of the 
#        neighboring pixels. The kernel is applied to every pixel 
#        in the image one-by-one to produce the final image 
#        (this operation known as a convolution).

img_rgb = cv2.imread('./resources/photos/bugatti-small.jpg')
img_grey = cv2.cvtColor(img_rgb, code= cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_rgb, (7, 7), 0)
img_canny = cv2.Canny(img_grey, 100, 100)
img_dial = cv2.dilate(img_canny, (5, 5), iterations=1)
img_ero = cv2.erode(img_canny, (5, 5), iterations=1)

if __name__ == '__main__':
    choices = {
        1: img_rgb,
        2: img_grey,
        3: img_blur,
        4: img_canny,
        5: img_dial,
        6: img_ero
    }
    choice = int(input('Enter the option : ')) 
    img = choices[choice]
    cv2.imshow('RGB image window', img)
    cv2.waitKey(0)