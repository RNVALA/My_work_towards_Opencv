import cv2 as cv
#loading a image
ronak_img=cv.imread('photos/a.jpg')
cv.imshow('paris',ronak_img)

#1converting to grayscale
gray = cv.cvtColor(ronak_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


#bluring a image
blur = cv.GaussianBlur(ronak_img,(7,7),cv.BORDER_DEFAULT)
#here first one is image name and second is image cornal, to blur image more and more you want to increse a kernl size
#then border type
cv.imshow('blur image',blur)


#edge cascade
ronak=cv.Canny(ronak_img,125,175)
#if we want to do more edge cascading then replace blur image inplace of ronak_img
cv.imshow('pedge cascade',ronak)

#dialating the  image
dilated =cv.dilate(ronak,(7,7),iterations = 3)
cv.imshow('dilated',dilated)


#eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroded image',eroded)
#here first we are eroding a dialating img so we put dialted image then kernel size and then iteration


#resizing
resized=cv.resize(ronak_img,(500,500),interpolation=cv.INTER_CUBIC)
#here in residing method we are just uploading img then how much size of a image and then interpolation
cv.imshow('resiging images',resized)

#cropping a image
cropped_image=ronak_img[ 50:200 , 200:400 ]#[rows,columns]
cv.imshow('croppedimage',cropped_image)
while True:
    if cv.waitKey(20) & 0xff==ord('x'):
        break

    