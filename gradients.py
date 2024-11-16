import cv2 as cv
import numpy as np

img= cv.imread('photos/pomidory.jpg')
cv.imshow('kit', img)

# laplacian
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey', grey)

lap = cv.Laplacian(grey, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)


# Sobel method
sobelx = cv.Sobel(grey, cv.CV_64F, 1, 0)
sobely = cv.Sobel(grey, cv.CV_64F, 0, 1)

cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)

cv.imshow('x_and_y', cv.bitwise_or(sobelx, sobely))


canny = cv.Canny(grey, 150 , 175)
cv.imshow('canny', canny)


cv.waitKey(0)