#resizing a image
#for interpolation
#if you are srinking the image you will probably go for
#default and if you are enlargiing the image then probably you use inter_linear or inter_cubic 
import cv2 as cv
ronak_img=cv.imread('photos/a.jpg')
cv.imshow('original image',ronak_img)



resized=cv.resize(ronak_img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized image',resized)






#fliping the image
#flip code must be 0-->fliping the image verticallyor ovet a x axis,
#1 specifies that you want to flip image horizontally or y axis
#-1 specifies flipping the imagr both vertically aswell as horizontally
flip = cv.flip(resized,0)
cv.imshow('flipped image',flip)

#cropping the image
cropped = ronak_img[200:400,300:400]
cv.imshow('croped image',cropped)
while True:
    if cv.waitKey(0) & 0xff==ord('x'):
        break
