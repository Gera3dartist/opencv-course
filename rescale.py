import cv2 as cv

img = cv.imread('photos/cat_bilolap.jpg')

cv.imshow('Cat', img)



def resise(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def change_res(width, height):
    # CAP_PROP_FRAME_WIDTH = 3
    # CAP_PROP_FRAME_HEIGHT = 4
    capture.set(cv.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, height)

capture = cv.VideoCapture('videos/cat_window.MOV')
   
while True:
    isTrue, frame = capture.read()
    print(f'has next: {frame is None}')
    frame_resized = resise(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



cv.waitKey(0)

cv.waitKey(0)


