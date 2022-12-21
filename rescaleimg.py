import cv2 as cv
#function start for rescaling the image
def rescaleing(image,w=0.5,h=0.5):
    width=int(image.shape[1] * w)#here 1 is width
    height=int(image.shape[0] * h)#where 0 is height
    dimension=(width,height)
    return cv.resize(image,dimension,interpolation=cv.INTER_AREA)
#function endas
#image reading


ronakimage=cv.imread('photos/a.jpg')#it will read a image
resized_img = rescaleing(ronakimage)#applying fun rescaling and storing output in resized_img
cv.imshow('image resize',resized_img)#it will show an image
cv.waitKey(0)


ronakimage.release()
cv.destroyAllWindows()

    
    