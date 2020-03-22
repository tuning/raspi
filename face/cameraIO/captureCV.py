#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 23:34:00 2020

@author: tutu

Example: Capture frames using openCV
"""

import cv2

# first camera id:0
cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'XVID')
framerate = 10.0
# VGA-resolution video by default
# use cv2.resize() to interpolate
resolution = (800,600)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,resolution[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,resolution[1])
cap.set(cv2.CAP_PROP_FPS,framerate)
HDresolution = (1600,1200)
out = cv2.VideoWriter('../pictures/vidCV.avi',codec,framerate,resolution)
outHD = cv2.VideoWriter('../pictures/vidCVHD.avi',codec,framerate,HDresolution)

while(True):
    ret,iframe = cap.read()
    out.write(iframe)
    iframeHD = cv2.resize(iframe,HDresolution,fx=0,fy=0,interpolation=cv2.INTER_CUBIC)
    outHD.write(iframeHD)
    cv2.imshow('Frame in video', iframe)
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        cv2.imwrite('../pictures/imgCV.jpg',iframe)
        cv2.imwrite('../pictures/imgCVHD.jpg',iframeHD)
        break
    
cap.release()
out.release()
outHD.release()
cv2.destroyAllWindows()