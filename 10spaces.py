import cv2 as cv
import matplotlib.pyplot as plt
#loading the original images
ronak_img=cv.imread('photos/a.jpg')
cv.imshow('original_images',ronak_img)

#inmatplot read image as a rgb formatmeans red,green and blue respectively
#but cv2 read as bgr reverse of rgb so there is difference in both the image
#plt.imshow(ronak_img)
#plt.show()

#bgr to grayscale
gray=cv.cvtColor(ronak_img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale image',gray)

#bgr to HSV hsv is also called huge saturation value
hsv=cv.cvtColor(ronak_img,cv.COLOR_BGR2HSV)
cv.imshow('hsv image',hsv) 


#bgr to lab means l*a*b
lab=cv.cvtColor(ronak_img,cv.COLOR_BGR2LAB)
cv.imshow('lab color',lab)
 
 
#converting bgr image into rgb
rgb=cv.cvtColor(ronak_img,cv.COLOR_BGR2RGB)
cv.imshow('rgb color',rgb) 
plt.imshow(rgb)
plt.show()

#we can't convert lab to rgb or bgr to hsv for that we want to convert to bgr and then bgr to _____
#here we are converting lab to bgr
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('labtobgr',lab_bgr)

while True:
    if cv.waitKey(0) & 0xff==ord('a'):
        break