import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

hue = [1.618705035971223, 180.0]
sat = [27.51798561151079, 255.0]
val = [0.0, 255.0]

#filePath = os.path
#print(filePath)

image = cv2.imread('C:\\Users\\fitzg\\Documents\\Python\\opencv\\photos\\ballTest.png')
image2 = cv2.imread('C:\\Users\\fitzg\\Documents\\Python\\opencv\\photos\\tech2.jpg')

image = cv2.resize(image,(500, 300))
blur = cv2.GaussianBlur(image,(101,101),8)
hsv_img = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
filtered_image = cv2.inRange(hsv_img, (hue[0], sat[0], val[0]),  (hue[1], sat[1], val[1]))
#cv2.imshow('Blur', filtered_image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(filtered_image, 100, 0.1, 20)

if corners is not None:
    print(len(corners))
    corners = np.int0(corners)
    for corner in corners:
        set = corner.ravel()
        x,y = set
        cv2.circle(image, (x,y), 5, (0,0,255), -1)
cv2.imshow('Image', image)

cv2.waitKey(0)