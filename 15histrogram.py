import cv2 as cv
import matplotlib.pyplot as plt
ronak_img=cv.imread('photos/a.jpg')
cv.imshow('original image',ronak_img)
#converting into grayscale images
gray= cv.cvtColor(ronak_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


#grayscale histrogram
#here we need to pass a list of images,chaneel and mask=none and then histsizeand range that is 0 to256
gray_hist = cv.calcHist([gray],[0],None ,[256],[0,256] )

plt.figure()
plt.title('Grayscale Histrogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)

#at x axis bins represent the intervals of pixel intensities 
#from output we can see that 120000 pixel  have 50 intensity