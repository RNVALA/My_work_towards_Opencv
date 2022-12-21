import numpy as np
import cv2 as cv

ronak_img=cv.imread('photos/a.jpg')


resized=cv.resize(ronak_img,(500,500))
cv.imshow('original image',resized)

blank = np.zeros(resized.shape[:2],dtype='uint8')
cv.imshow('blank image',blank)

mask = cv.circle(blank,(resized.shape[1]//2,resized.shape[0]//2),100,255,-1)
cv.imshow('circle',mask)

masked = cv.bitwise_and(resized,resized,mask=mask)
cv.imshow('Masked image',masked)

cv.waitKey(0) 

