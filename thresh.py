import cv2 as cv
import numpy as np
import  matplotlib.pyplot as plt

# img = cv.imread('photos/cat_bilolap.jpg')
# img = cv.imread('photos/orto_dvir.jpg')
img = cv.imread('photos/pomidory.jpg')
cv.imshow('bilolap', img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(grey, 150, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

threshold_inv, thresh_inv = cv.threshold(grey, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh_inv', thresh_inv)


# adaptive

adaptive_thresh = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, C=3)
cv.imshow('adaptive_thresh', adaptive_thresh)


adaptive_thresh_gaus = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, C=3)
cv.imshow('adaptive_thresh_gaus', adaptive_thresh_gaus)
cv.waitKey(0)