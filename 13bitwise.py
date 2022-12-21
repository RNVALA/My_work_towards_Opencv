import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
#herre30,30 is starting point 370,370 is ending point 255 is color and-1 is filled 
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
#here 200,200 is point on which circle center , 200 is diameter and 255 is color and -1 is colored filled

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise AND
#it place both the image on top of each other and basically returned the intersection.
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise And',bitwise_and)

#bitwise OR
#it place a image that are common to both of the image and area that are not common to both of the image 
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise OR',bitwise_or)
 
#bitwise XOR
#bitwise XOR which is basically  for non intersecting area
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise xoring',bitwise_xor)

#bitwise not means it will invert the color black to white or vice-versa
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise not',bitwise_not)
cv.waitKey(0)