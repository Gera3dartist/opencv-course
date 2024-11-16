import cv2 as cv
import numpy as np

img = cv.imread('photos/cat_bilolap.jpg')
# print(img.shape)




def resise(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)




resized_img = resise(img, scale=0.2)
# cv.imshow('Cat', resized_img)

print(f'resized_img.shape: {resized_img.shape}')

blank = np.zeros((500, 500, 3), dtype='uint8')

# blank[400:500, 400:500 ] = 0, 255, 0
# cv.imshow('Box', blank)

# 1. Draw a rectangle

cv.rectangle(blank, (100, 100), (blank.shape[1]//2, blank.shape[0]//2), (234,0, 0), thickness=-1)
cv.rectangle(blank, (200, 200), (300, 300), (0, 255, 0), thickness=2)

# 2. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), radius=100, color=(0, 0, 255), thickness=2)


# 3. Draw a line
cv.line(blank, (0, 0), (500, 500), color=(0, 255, 0), thickness=2)


# 4. Put text
text = '''the 
text'''
cv.putText(blank, text, (100, 100), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=2.0, thickness=2, color=(255, 255, 255))
cv.imshow('Blank', blank)






# def change_res(width, height):
#     # CAP_PROP_FRAME_WIDTH = 3
#     # CAP_PROP_FRAME_HEIGHT = 4
#     capture.set(cv.CAP_PROP_FRAME_WIDTH, width)
#     capture.set(cv.CAP_PROP_FRAME_HEIGHT, height)

# capture = cv.VideoCapture('videos/cat_window.MOV')
   
# while True:
#     isTrue, frame = capture.read()
#     print(f'has next: {frame is None}')
#     frame_resized = resise(frame, scale=0.2)

#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()




cv.waitKey(0)


