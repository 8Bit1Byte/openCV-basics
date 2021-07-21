import cv2
import numpy as np

frame_resolution = (600, 400)
vidWri = cv2.VideoWriter('./test.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, frame_resolution)

img_back = np.zeros((400, 600, 3), np.uint8)
colors_plate = [(255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
i = 0
c = 0

while True:
    i += 1
    vidWri.write(img_back)
    if i < 100:
        cv2.rectangle(img_back, (0, 0), (i, i), colors_plate[c], cv2.FILLED)
    else:
        i = 0
        c += 1
    cv2.imshow('Video', img_back)

    if cv2.waitKey(34) & 0xFF == ord('q'):
        break

vidWri.release()

cv2.destroyAllWindows()
   
print("The video was successfully saved")