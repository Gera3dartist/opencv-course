import cv2 as cv
import numpy as np
import  matplotlib.pyplot as plt

# img = cv.imread('photos/cat_bilolap.jpg')
# img = cv.imread('photos/orto_dvir.jpg')
img = cv.imread('photos/pomidory.jpg')
cv.imshow('bilolap', img)



blank = np.zeros(img.shape[:2], dtype='uint8')
circl = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), radius=100, color=255,  thickness=-1)
cv.imshow('circle', circl)


# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)
# mask = cv.bitwise_and(gray, gray, mask=circl)
# cv.imshow('mask', mask)



# gray_hist = cv.calcHist([gray], [0], circl, [256], [0, 256])
# plt.figure()
# plt.title('Greyscale hist')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.xlim((0, 256))
# plt.plot(gray_hist)
# plt.show()


# color historgram
plt.figure()
plt.title('Greyscale hist')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
 

mask_rgb = cv.bitwise_and(img, img, mask=circl)
cv.imshow('mask_rgb', mask_rgb)
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], circl, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim((0, 256))
plt.show()

cv.waitKey(0)