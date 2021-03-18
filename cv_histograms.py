import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

#filePath = os.path
#print(filePath)

image = cv2.imread('C:\\Users\\fitzg\\Documents\\Python\\opencv\\photos\\ballTest.png')
image2 = cv2.imread('C:\\Users\\fitzg\\Documents\\Python\\opencv\\photos\\tech2.jpg')

#Gray Histogram
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_hist = cv2.calcHist([gray_image], [0], None, [256], [0,256])
plt.figure()
plt.title('Histogram')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#Color Histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
chColors = ('Blue', 'Green', 'Red')

for i in range(0, 3):
    color_hist = cv2.calcHist([image2], [i], None, [256], [0,256])
    plt.plot(color_hist, color=chColors[i])
    plt.xlim([0,256])

plt.show()



cv2.waitKey(0)