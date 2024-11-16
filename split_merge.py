import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/cat_bilolap.jpg')

blank = np.zeros(img.shape[:2], dtype=np.uint8)


cv.imshow('Bilolap', img)


b,g,r = cv.split(img)


cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(f'Img: {img.shape}')
print(f'blue {b.shape}')
print(f'green {g.shape}')
print(f'red {r.shape}')


merged = cv.merge([b,g, r])
cv.imshow('merged', merged)

# show channel with color

cv.imshow('blue', cv.merge([b, blank, blank]))
cv.imshow('green', cv.merge([blank, g, blank]))
cv.imshow('red', cv.merge([blank, blank, r]))

cv.waitKey(0)