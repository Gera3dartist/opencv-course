import os
import cv2 as cv
import numpy as np
from pathlib import Path


img = cv.imread('photos/female_face_2.png')
# img = cv.imread('photos/female_face_1.webp')

cv.imshow('face', img)
print (type(img))
FACES  = Path('Resources/Faces')
FACES_TRAIN = FACES /'train'
people = os.listdir(FACES_TRAIN)

features = []
labels = []

def pre_process_image(img: np.ndarray):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = FACES_TRAIN / person
        # get index of certain person's folder, so we represent a person 
        # with a numerical id 
        label = people.index(person)
        for img in os.listdir(path):
            cv_img = cv.imread(path / img)
            gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, 1.1, minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                # roi - region of interest
                # go and extract faces
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

features = np.array(features, dtype='object')
labels =   np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.train(features, labels)

face_recognizer.save('face_trainde.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)



cv.waitKey(0)