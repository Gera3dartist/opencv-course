from pathlib import Path
import cv2 as cv
import numpy as np


haar_cascade = cv.CascadeClassifier('haar_face.xml')
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trainde.yml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Mindy Kaling', 'Madonna']

FACES  = Path('Resources/Faces')


# ----  Validation  ----

ben = FACES / 'val' / 'ben_afflek' / '2.jpg'
elton = FACES / 'val' / 'elton_john' / '3.jpg'
jerry = FACES / 'val' / 'jerry_seinfeld' / '3.jpg'
madonna = FACES / 'val' / 'madonna' / '3.jpg'

samples = [
    ben, 
    elton,
    jerry,
    madonna
]


for person in samples:
    img = cv.imread(person)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # grab folder name
    person.parent
    cv.imshow(str(person.parent), gray)
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
    label = 'unknown'
    for (x,y,w,h) in faces_rect:
        # check if that works
        face_roi = gray[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(face_roi)
        print(f'Label: {people[label]} with confidence {confidence}')
        cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
        cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv.imshow(f'Detecting {person.parent}', img)

    
cv.waitKey(0)
