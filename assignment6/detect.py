import cv2
import numpy as np
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

video = cv2.VideoCapture('walking.avi')

while video.isOpened():
    

    ret, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == ord('q'): 
        break

video.release()
cv2.destroyAllWindows()
