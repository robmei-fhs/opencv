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
image2 = cv2.imread('C:\\Users\\fitzg\\Documents\\Python\\opencv\\photos\\ballTest2.png')

image = cv2.resize(image,(500, 300))
blur = cv2.GaussianBlur(image,(101,101),8)
hsv_img = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
filtered_image = cv2.inRange(hsv_img, (hue[0], sat[0], val[0]),  (hue[1], sat[1], val[1]))
#cv2.imshow('Blur', filtered_image)
gray_image = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(filtered_image, 10, 100)
contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#print("Number of Contours is: " + str(len(contours)))

for c in range(len(contours)):
    
    cv2.drawContours(image, contours, c, (255, 0, 0), 6)

    m = cv2.moments(contours[c])
    #print(m.keys())

    print("Area: " + str(cv2.contourArea(contours[c])))
    print("Arc Length: " + str(cv2.arcLength(contours[c], True)))
    
    #Find the center
    cx = int(m['m10'] / m['m00'])
    cy = int(m['m01'] / m['m00'])
    cv2.circle(image, (cx, cy), 2, (0,0,255),-1)

    #Bounding Rectangle
    x, y, w, h = cv2.boundingRect(contours[c])
    cv2.rectangle(image, (x, y), (x+w, y+h), color = (0, 255, 0), thickness = 2)

    cv2.putText(image, ('Name: Contour ' + str(c)), (x, y+h + 15), cv2.FONT_HERSHEY_SIMPLEX, .35, (0,255,0), 1, cv2.LINE_AA)

image2 = cv2.resize(image2,(500, 300))
blur2 = cv2.GaussianBlur(image2,(101,101),8)
hsv_img2 = cv2.cvtColor(blur2, cv2.COLOR_BGR2HSV)
filtered_image2 = cv2.inRange(hsv_img2, (hue[0], sat[0], val[0]),  (hue[1], sat[1], val[1]))

edges2 = cv2.Canny(filtered_image2, 10, 100)
contours2, hierarchy2 = cv2.findContours(edges2,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in range(len(contours2)):
    
    cv2.drawContours(image2, contours2, c, (255, 0, 0), 6)
    
    peri = cv2.arcLength(contours2[c], True)
    approx = cv2.approxPolyDP(contours2[c], .02*peri, True)
    print(len(approx))
    
    m = cv2.moments(contours2[c])
    #print(m.keys())

    #print("Area: " + str(cv2.contourArea(contours2[c])))
    #print("Arc Length: " + str(cv2.arcLength(contours[c], True)))
    
    #Find the center
    cx = int(m['m10'] / m['m00'])
    cy = int(m['m01'] / m['m00'])
    cv2.circle(image2, (cx, cy), 2, (0,0,255),-1)

    #Bounding Rectangle
    x, y, w, h = cv2.boundingRect(contours2[c])
    cv2.rectangle(image2, (x, y), (x+w, y+h), color = (0, 255, 0), thickness = 2)

    cv2.putText(image2, ('Name: Contour ' + str(c)), (x, y+h + 15), cv2.FONT_HERSHEY_SIMPLEX, .35, (0,255,0), 1, cv2.LINE_AA)


cv2.imshow('Image', image)
cv2.imshow('Image 2', image2)
cv2.waitKey(0)