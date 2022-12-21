import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

ronak_img=cv.imread('photos/a.jpg')
resize=cv.resize(ronak_img,(500,500))
cv.imshow('resizedimg or original image',resize)

blank=np.zeros(resize.shape[:2],dtype='uint8')

circle=cv.circle(blank,(resize.shape[1]//2,resize.shape[0]//2),100,255,-1)

masked=cv.bitwise_and(resize,resize,mask=circle)
cv.imshow('masked image',masked)

#color histrogram
plt.figure()
plt.title('color histrogram')
plt.xlabel('bins')
plt.ylabel('# of pixel')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([resize],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()    
cv.waitKey(0)

