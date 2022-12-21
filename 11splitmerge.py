import cv2 as cv
import numpy as np

ronak_img=cv.imread('photos/a.jpg')
cv.imshow('original value',ronak_img)

#creating blank image 
blank=np.zeros(ronak_img.shape[:2],dtype='uint8')

#splliting the image into b,g,r
b,g,r = cv.split(ronak_img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

#now shape of splittes image
print(ronak_img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merging of a image
merged=cv.merge([b,g,r])
cv.imshow('merged image',merged)

cv.waitKey(0)
