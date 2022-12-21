import cv2 as cv
 #staring the web cam
capture_video=cv.VideoCapture(0)#0 for web cam

while True:
    #read video frame by frame
    isTrue,frame=capture_video.read()

    canny_edge=cv.Canny(frame,120,150)

    #showing the edges video
    cv.imshow('edges video',canny_edge)
    #displaying real web cam
    cv.imshow('Real web cam',frame)
    if cv.waitKey(0) & oxff == ord('x'):
        break
