import cv2 as cv

img = cv.imread('photos/cat_bilolap.jpg')

cv.imshow('Cat: ', img)

# 1. convert to GreyScale
img_grey = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow('Cat gray', img_grey)


# 2. Blur
blur = cv.GaussianBlur(img, ksize=(3, 3), sigmaX=10, borderType=cv.BORDER_DEFAULT)
cv.imshow('Blured cat', blur)

# 3. Edge Cascade
canny = cv.Canny(img, threshold1=125, threshold2=175)
cv.imshow('Edges', canny)

# 4.  To increase edges pass blured image
canny_blured = cv.Canny(blur, threshold1=125, threshold2=175)
cv.imshow('Edges blured', canny_blured)

# 5. dilate image (make wider edges)
img_dilated = cv.dilate(canny_blured, (7,7), iterations=1)
cv.imshow('Dilated', img_dilated)

# 6. Erode
# it cancels an effect of dilate, given the equivalent kernel size and iterations number, 
# to be defined experimenting
erode_img = cv.erode(img_dilated, (7, 7), iterations=1)
cv.imshow('Erode', erode_img)

# 7. resize

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized', resized)

# 8. cropped
cropped = img[1000:1500, 800:1300]
cv.imshow('Cropped', cropped)



cv.waitKey(0)