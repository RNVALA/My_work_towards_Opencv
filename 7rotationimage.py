import cv2 as cv
import numpy as np
ronak_img = cv.imread('photos/a.jpg')
cv.imshow('original image',ronak_img)#displaying the original image
#rotation of a image
def rotate(ronak_img,angle,rotpoint=None):
    (height,width)=ronak_img.shape[:2]
    #here:2 means it will take shape as 0 and 1 respectively
    if rotpoint is None:
        rotpoint = (width//2,height//2)
        #means if you will not give rotpoint then it will automatically rotate from center
    rotmat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
    #upper line is 2d matrix to rotate the image according to the parameter values passed
    #here floting point 1.0 that specifies the scale of the rotated image in relation to the 
    #original image.here1.0 tells rotate image at same dimensions as original images
    #higher scale value expands the image while lower value shrinks the image
    dimensions=(width,height)
    
    return cv.warpAffine(ronak_img,rotmat,dimensions)

rotated_img=rotate(ronak_img,45)#here +45 so image will rotate in clockwise direction
#if you will give - parameter then it will rotate in anti clockwise direction
cv.imshow('rotate',rotated_img)

cv.waitKey(0)
    
