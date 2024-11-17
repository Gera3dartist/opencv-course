import cv2
import numpy as np
import time

face_clacifier  = cv2.CascadeClassifier("haar_face.xml")

videoCam = cv2.VideoCapture(0)

if not videoCam.isOpened():
    print("Camera is not opened")
    exit()

should_exit = False
while (should_exit == False):
    ret, frame = videoCam.read()
    cv2.imshow("Frame", frame)

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", gray)
        detected_faces = face_clacifier.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 3)

        for (x, y, w, h) in detected_faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        

        text = "Found faces = " + str(len(detected_faces))

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text, (0, 30), font, 1, (255, 0, 0), 1)

        cv2.imshow("Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            should_exit = True
            break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        should_exit = True
        break

videoCam.release()
cv2.destroyAllWindows()


