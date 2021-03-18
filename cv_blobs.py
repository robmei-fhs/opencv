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
gray_image = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

blobDetector = cv2.SimpleBlobDetector()
blobs=None
blobs = blobDetector.detect(gray_image)
print(len(blobs))
if blobs is not None:
    im_with_keypoints = cv2.drawKeypoints(image, blobs, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('Image', im_with_keypoints)
else:
    cv2.imshow('Image', image)

cv2.waitKey(0)