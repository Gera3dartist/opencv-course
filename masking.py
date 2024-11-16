import cv2 as cv
import numpy as np

img = cv.imread('photos/cat_bilolap.jpg')
img = cv.imread('photos/orto_dvir.jpg')
cv.imshow('bilolap', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank image', blank)

# # mask = cv.circle(blank, (img.shape[1]//2+100, img.shape[0]//2 - 200), radius=700, color=255,  thickness=-1)
# mask = cv.rectangle(
#     blank, 
#     pt1=(img.shape[1]//2-500, img.shape[0]//2-600),
#     pt2=(img.shape[1]//2+700, img.shape[0]//2+400),
#     color=255,  thickness=-1)
# cv.imshow('Mask', mask)

# masked = cv.bitwise_and(img, img, mask=mask)
# cv.imshow('Masked', masked)
# cv.imshow('Mask', mask)


rec = cv.circle(blank.copy(), (img.shape[1]//2+100, img.shape[0]//2 - 200), radius=700, color=255,  thickness=-1)
cir = cv.rectangle(
    blank.copy(), 
    pt1=(img.shape[1]//2-500, img.shape[0]//2-800),
    pt2=(img.shape[1]//2+700, img.shape[0]//2+300),
    color=255,  thickness=-1)
xor = cv.bitwise_or(rec, cir)
cv.imshow('xor', xor)



masked = cv.bitwise_and(img, img, mask=xor)
cv.imshow('Masked', masked)



cv.waitKey(0)