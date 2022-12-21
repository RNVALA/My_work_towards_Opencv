#opencv has lot of pre trained classifier we can use it
# two main classifier exist today is
# har cascades and core binary patterns
# after copying har cascades xml codes.
# to xml file over classifier is ready
import cv2 as cv

image = cv.imread('photos/kohli.jpg')
image=cv.resize(image,(700,700))
cv.imshow('meet',image)

#first we have to convert it to gray scale because it can not detect skintone or color 
# look at edges and try to deternmine it is image or not 
#so we will convert it to gray scale

gray= cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('gray_image',gray)

haar_cascade = cv.CascadeClassifier('D:/opencv/.vscode/advance_open_cv/faces/haar_face.xml')#opening xml file of haar cascade classifier
faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=1)
#scale_factor specifies the scale by which the size of the image must be reduced and
#min_neighbours specifies the number of rectangles each rectangle should have.

#here faces will be in rectangle formate and minNeghbour means minimum neighbours rectangle need to be called    
print('total faces in image are',len(faces))
# as we know that faces is in rectangle shape so we can print that rectangle
#below w,x,y,z are coordinte of an rectangle so we are drawing it
for (w,x,y,z) in faces:
    cv.rectangle(image,(w,x),(w+y,x+z),(0,255,0),thickness=2)
cv.imshow('detected_image',image)
cv.waitKey(0)