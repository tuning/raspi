#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:07:14 2020

@author: tutu

Now we combine face detection and recognition.
"""

import datetime
import cv2

faceDetector = cv2.CascadeClassifier('./etc/haarcascade_frontalface_default.xml')
boxColor = (0,128,255)
faceImageSize = (300,300)
minFaceSize = (100,100)
maxFaceSize = (300,300)

faceRecognizer = cv2.face.createLBPHFaceRecognizer()
faceRecognizer.load('./faces/model/faceRecModel.yml')
labels = {'1':'fangfang','2':'tutu','3':'yaoyao','4':'zhangzhang','5':'nainai'}
textFont = cv2.FONT_HERSHEY_PLAIN
textSize = 2
textColor = (0,255,0)
textWidth = 2

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
        personId = faceRecognizer.predict(faceImage)

        # mark the face in the frame and display the frame
        cv2.rectangle(iframe, (faceBox[0],faceBox[1]),
                      (faceBox[0]+faceBox[2],faceBox[1]+faceBox[3]),boxColor, 2)
        cv2.putText(iframe,labels[str(personId[0])],(x,y),textFont,textSize,textColor,textWidth)
        cv2.putText(iframe,str(personId[1])+'%',(x,y+h),textFont,textSize,textColor,textWidth)
        cv2.imshow('Face detector',iframe)
        
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()