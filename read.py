import cv2 as cv 
#img = cv.imread('photos/a.jpg')
#cv.imshow('a',img)#it 
#cv.waitkey(0)#it is keyboard binding function, it wait for a specific delay or time in millisecond

  #reading videos
capture = cv.VideoCapture('videos/ab.mp4')
while True:
    istrue, frame = capture.read()
    cv.imshow('videos' , frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        #here we will press d then also it will break the loop
        break
capture.release()#Closes video file
cv.destroyAllWindows()#function allows users to destroy or close all windows at any time after exiting the script.
