#here we are creating the binary image from a standard image
#here two threshholding 1. simple threshholding and adaptive threshholding
import cv2 as cv

original_img=cv.imread('photos/a.jpg')
original_img=cv.resize(original_img,(500,500))
cv.imshow('original image',original_img)

gray = cv.cvtColor(original_img,cv.COLOR_BGR2GRAY)
cv.imshow('grayimage',gray)
#SIMPLE THRESHHOLDING
#here essentially we use cv.threshhold function and this function return threshhold and thresh
#here we are giving parameter as src image,threshhold value,max value,threshhold_type here we are using cv.THRESH_BINARY
#here we are setting threshhold 150 then maxvalue 255 so max value means if image is more than 145 then it will convert into 255 in this case
#IF PIXEL VAlue is less than 145 than it will converting into 0
threshhold , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('simple Threshhold',thresh)
#threshold inverse
threshhold,thresh_inver=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('simple inverse',thresh_inver)
#adaptive thresholding that essebtially computing the threshhold value on the bssis of mean  
#here in parameter we provide sorce image, max threshold,adaptive method,then threshold type,then kernel size,then c value that is value that is substracted from mean value 
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,0)
cv.imshow('adaptivr threshold',adaptive_thresh)
cv.waitKey(0)