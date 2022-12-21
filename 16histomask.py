import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

ronak_img=cv.imread('photos/a.jpg')

resized=cv.resize(ronak_img,(500,500))
cv.imshow('resized image',resized)

blank=np.zeros(resized.shape[:2],dtype='uint8')


gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow('gray image',gray)

circle=cv.circle(blank,(resized.shape[1]//2,resized.shape[0]//2),100,255,-1)
cv.imshow('mask',circle)

mask=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('mask',mask)
#grayscale histrogram
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('grayscale Histrogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([ 0,256])
plt.show()

cv.waitKey(0)
    

