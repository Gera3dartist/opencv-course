"""
The contours are different from edges, we need them as building blocks for segmentation and detection

"""
import cv2 as cv
import numpy as np

img = cv.imread('photos/cat_bilolap.jpg')
cv.imshow('bilolap', img)


# converts to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#blur
# -> comment
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

# cv.imshow('blured', blur)

# detect edges
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny edges', canny)



# # looks after structure of elements, countrour - list of coordinates of countour.
# # hierarchies - represenation o
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)}')

## end -> comment



ret, thresh = cv.threshold(gray, 160, 255, type=cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)}')

# add blank image

blank = np.zeros(img.shape[:2], dtype=np.float32)

cv.drawContours(blank, contours=contours, contourIdx=-1, color=(255, 255, 255), thickness=2)
cv.imshow('Contours', blank)


cv.waitKey(0)