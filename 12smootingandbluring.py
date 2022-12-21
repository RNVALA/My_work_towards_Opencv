import cv2 as cv

ronak_img=cv.imread('photos/a.jpg')
#cv.imshow('original image',ronak_img)
resized=cv.resize(ronak_img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized image',resized)


#bluring the image by averaging
average = cv.blur(resized,(7,7))#here 3,3 is kernel size if you want to blur more than increse kernel size
cv.imshow('average blur',average)


#gausian blur
gauss= cv.GaussianBlur(resized,(7,7),5)
cv.imshow('gausian blur',gauss)

#median blur
median=cv.medianBlur(resized,7)
cv.imshow('median blur',median)


#bilstral blur
bilateral = cv.bilateralFilter(resized,10,35,24)
cv.imshow('Bilateral image',bilateral)
cv.waitKey(0) 