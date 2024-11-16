import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/cat_bilolap.jpg')

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('Bilolap', img)


plt.imshow(img)
plt.show()

# BRG to gscale

gscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('GreyScale', gscale)


# BGS to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)


# BGS to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)


# BGR to rgb

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

cv.waitKey(0)