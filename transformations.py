import cv2 as cv
import numpy as np

img = cv.imread('photos/cat_bilolap.jpg')
cv.imshow('BLLAP', img)

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    #            width           height
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)
    



translated = translate(img, -1500, -600)
cv.imshow('Translated', translated)



# Rotation
def rotate(img, angle, center = None):
    (width, height) = img.shape[:2]
    if center is None:
        center = (width//2, height//2)
    rot_matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    print(f'>> rot_matrix: {rot_matrix}')
    return cv.warpAffine(img, rot_matrix, (width, height))

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)


# Resizing

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
# cv.imshow('Resized', resized)

# flipped

flipped = cv.flip(img, 1)

cv.imshow('flipped-1', cv.flip(img, -1))
cv.imshow('flipped0', cv.flip(img, 0))
cv.imshow('flipped1', cv.flip(img, 1))

# cropping
cv.imshow('cropped', img[200:500, 300:7000])

cv.waitKey(0)