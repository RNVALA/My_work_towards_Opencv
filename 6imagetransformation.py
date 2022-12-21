import cv2 as cv
import numpy as np

ronak_img = cv.imread('photos/a.jpg')
cv.imshow('original_image',ronak_img)


#translation
#translation refers to a rectillinear shift of a object i.e an image from one place to another
def translate(ronak_img,x,y):#here x means amount of move horizontal and y means amount of move vertically
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions = (ronak_img.shape[1],ronak_img.shape[0])
    return cv.warpAffine(ronak_img,transMat,dimensions)
    #here we use warpaffine to transform the image

#here -x--->left 
#here -y--->up 
#here x--->right 
#here y--->down 
translated = translate(ronak_img,100,100)
cv.imshow('translated_img',translated)

cv.waitKey(0)