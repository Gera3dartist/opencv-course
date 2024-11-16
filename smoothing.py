import cv2 as cv


img = cv.imread('photos/cat_bilolap.jpg')
cv.imshow('nomral', img)

size = 27

# averaging
average = cv.blur(img, (size, size))
cv.imshow('average blur', average)

# gaussian
# computes average and gives weights
gauss = cv.GaussianBlur(img, (size, size), 0)
cv.imshow('gaus', gauss)

# mean - finds mean

mean = cv.medianBlur(img, size)
cv.imshow('median', mean)


# bilateral 

bilateral =  cv.bilateralFilter(img, d=21, sigmaColor=15, sigmaSpace=15)
cv.imshow('bilateral', bilateral)
cv.waitKey(0)