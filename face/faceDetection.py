#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:43:30 2020

@author: tutu

Continuous face detection using Haar Cascade classifier
Save face images in faces dir to train face recognition model
"""
import numpy as np
import datetime
import cv2

faceDetector = cv2.CascadeClassifier('./etc/haarcascade_frontalface_default.xml')
boxColor = (0,128,255)
faceImageSize = (300,300)
minFaceSize = (100,100)
maxFaceSize = (300,300)

# first camera in the system
cap = cv2.VideoCapture(0)
framerate = 3.0
resolution = (800,600)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,resolution[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,resolution[1])
cap.set(cv2.CAP_PROP_FPS,framerate)

frameCounter = 0
while True:
    ret,iframe = cap.read()
    frameCounter = frameCounter+1
    nowTime=datetime.datetime.now()
    faceImageFileName = './faces/face'+nowTime.strftime('%y%m%d%H%M%S')+str(frameCounter)+'.png'
    
    # detection on the grayscale image
    iframeGray = cv2.cvtColor(iframe,cv2.COLOR_BGR2GRAY)
    faceBoxes = faceDetector.detectMultiScale(
            iframeGray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=minFaceSize,
            maxSize=maxFaceSize)
    
    # select the largest box
    if len(faceBoxes) >= 1:
        # detected
        maxArea = 0
        x = 0
        y = 0
        w = 0
        h = 0
        for (_x,_y,_w,_h) in faceBoxes:
            if  _w*_h > maxArea:
                x = _x
                y = _y
                w = _w
                h = _h
                maxArea = w*h
        faceBox = (x,y,w,h)
        
        # save face image to file after scaling
        faceImage = iframeGray[y:y+h,x:x+w]
        faceImage = cv2.resize(faceImage,faceImageSize,fx=0,fy=0,interpolation=cv2.INTER_CUBIC)
        if (np.mod(frameCounter,2)==1):
            cv2.imwrite(faceImageFileName,faceImage)
        
        # mark the face in the frame and display the frame
        cv2.rectangle(iframe, (faceBox[0],faceBox[1]),
                      (faceBox[0]+faceBox[2],faceBox[1]+faceBox[3]),boxColor, 2)
        cv2.imshow('Face detector',iframe)
        
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()