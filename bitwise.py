import cv2 as cv
import numpy as np

# img = cv.imread('photos/cat_bilolap.jpg')
# cv.imshow('bilolap', img)

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370),  255, -1)

circle = cv.circle(blank.copy(), center=(blank.shape[1]//2, blank.shape[0]//2), radius=blank.shape[1]//2, color=(255, 255, 255), thickness=-1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)


# bitwise AND -- intersecting
cv.imshow('bitwise_and', cv.bitwise_and(circle, rectangle))
# bitwise OR -- intersecting and none intersecting
cv.imshow('bitwise_or', cv.bitwise_or(circle, rectangle))
# bitwise XOR -- none intersecting
cv.imshow('bitwise_xor', cv.bitwise_xor(circle, rectangle))
# bitwise NOT -- invets
cv.imshow('bitwise_not', cv.bitwise_not(rectangle))
# bitwise NOT -- invets
cv.imshow('bitwise_not_circle', cv.bitwise_not(circle))

cv.waitKey(0)