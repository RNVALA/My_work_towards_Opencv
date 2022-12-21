import cv2 as cv
import numpy as np
original_img=cv.imread('photos/a.jpg')
original_img=cv.resize(original_img,(500,500))
cv.imshow('original image',original_img)

gray=cv.cvtColor(original_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray image',gray)

#Laplacia
#in this we pass parameter as src image
lap = cv.Laplacian(gray,cv.CV_64F)#here we are detecting the edges or gradient of gray imagge with destination depth cv.Cv_64F
#the cv.Laplacian() method detects the gradients for black and white, and due to its vector nature, it converts some of its slope to negative, resulting in negative pixels.
lap = np.uint8(np.absolute(lap))#now we are setting lap values to absolute using the np.unit8() method #convert all-ve pixels to positives
cv.imshow('laplacian image ',lap)

#sobel
#sobel edge detection detects the gradient of a image in two directions, X and Y axes.
#in x direction, we use cv.Sobel(sourceimage,cv.CV_64F,1,0)
#when we detect the gradient in y direction  we use cv.sobel(sourceimage,cv.CV_64F,0,1)
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

#convert all negative pixels to positives
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))

#now displaying the image
cv.imshow('sobel x edges ',sobelx)
cv.imshow('sobel y edges',sobely)

#canny method
canny= cv.Canny(gray,150,175)
cv.imshow('canny image',canny)

cv.waitKey(0)

#note 
#im most of case cv.canny method to detect edges in an image
#and laplacian and sobel method are generally used to detect the gradient and with this two method, you need to convert negative pixels to their absolute value using np.absolute