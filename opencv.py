# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:27:35 2024

@author: James
"""
#import opencv
import cv2

#locate library used for face cascade classification and store it
face_cascade = cv2.CascadeClassifier("/Users/James/Desktop/haarcascade_frontalface_default.xml")
#video willbe captured on the front camera 
video=cv2.VideoCapture(0)


address = "https://10.49.10.50:8080/video"

video.open(address)

while True:
    check,frame=video.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,
        scaleFactor=1.1,
        minNeighbors=5 )
    for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('Video',frame)
    
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows
    