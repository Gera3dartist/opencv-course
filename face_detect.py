import cv2 as cv

img = cv.imread('photos/female_face_2.png')
# img = cv.imread('photos/female_face_1.webp')

cv.imshow('face', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('gray', gray)


# using haar cascade

haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'NUmber of faces found: {len(face_rect)}')

for (x,y,w,h) in face_rect:
    print(x,y,w,h)
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)


cv.imshow('Detected faces', img)

cv.waitKey(0)