import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')# it will show a blank image of500*500
cv.imshow('blanlk image',blank)

#abc=cv.imread('photos/a.jpg')
#cv.imshow('paris',abc)

#1.we are painting the blank images
#blank[:]=0,255,0#all image will be green
#blank[200:300,300:400]=0,255,0#here some part of a image will be coloured as per given pixcels
#cv.imshow('Green',blank)


#2.drawing rectanglr
cv.rectangle(blank,(0,0),(250,500),(0,250,0),thickness=cv.FILLED)
#here starting point is0,0 AND 250,250 is destination and 0,250,0 is color
cv.imshow('rectangke',blank)

#3.drawing circle
cv.circle(blank,(250,250) , 100,(0,0,255),thickness=cv.FILLED)
#here  250,250 is location of a radius point  100 is radius of a circle and last one is color
cv.imshow('circle',blank)

#4.draw a line
cv.line(blank,(100,250),(25,250),(255,255,255),thickness=4)
#here a 0,0 is starting point and 250,250 is ending point and 255,255,255 is color
cv.imshow('line',blank)
#5 write a text on a image
cv.putText(blank,'hello my name is ronak',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=4)
#here  blank is page of500*500 and then name and 225,225 is starting point of a text and then font and then color
cv.imshow('text',blank)
while True:
    if cv.waitKey(20) & 0xff==ord('x'):
        break

