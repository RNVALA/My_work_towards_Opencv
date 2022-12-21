#the contours are the useful tool for shape analysis and object detection and reognition
#to maintain accuracy we apply canny edge detection 
#opencv provides findcontours() which is used to find the contour in binary image
#findcontour accepts 3 argument 1)source image 2.)contour reteival mode 3.)contour approximation


import numpy as np
import cv2 as cv


#reading a image
ronak_img=cv.imread('photos/a.jpg')
cv.imshow('original_image',ronak_img)

blank=np.zeros(ronak_img.shape,dtype='uint8')
cv.imshow('blank image',blank)

#converting image into gray
gray = cv.cvtColor(ronak_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray_image',gray)

#NOW WE ARE BLURING THE IMAGE WITHOUT BLURING WE FOUND MORE CONTOURS
blur= cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blurimages',blur)
#converting into canny image
canny=cv.Canny(blur,125,175)
cv.imshow('canny_image',canny)

#we can contourby another method called thresh
#ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
#cv.imshow('Thresh images',thresh)

#contour method
contours, hierarchies = cv.findContours(canny ,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#SINCE CONTOUR IS LIST SO WE CAN PRINT THE LENGTH OF A LIST
print(f'{len(contours)} contours fond')
#here cv.RETR_LIST-
#HERE CV.CHAIN_APPROX_SIMPLE-->WHICH ESSENTIALLY COMPRESSES ALL THE QUANTITIES THAT ARE RETURNED MEANS 


#displaying the contour in blank image
cv.drawContours(blank,contours,-1,(255,0,0),2)#here -1 to display all the contours and 2 is thickness
cv.imshow('contour_drawn',blank)
cv.waitKey(0)



#note  
#without bluring the image we found that contours found more as compare to original images
