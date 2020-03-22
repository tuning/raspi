#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:22:53 2020

@author: tutu

Example: Capture frames using PiCamera
"""

from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
from time import sleep

# capture image from camera
camera = PiCamera()
camera.rotation = 0
camera.resolution = (480,320)
camera.framerate = 25
camera.annotate_text = "copyright @tutu"
camera.brightness = 60
camera.image_effect = "none"
camera.exposure_mode = "auto"
camera.awb_mode = "auto"

# taking a still picture
# use PiRGBArray as we need the raw image, e.g., the
# color tensor instead of the compressed jpg image
frame = PiRGBArray(camera)
sleep(1)
camera.capture(frame,format='bgr')
image = frame.array
cv2.imshow('Still image',image)
cv2.waitKey(0)

# capture video
frame = PiRGBArray(camera, size=(480,320))
sleep(1)
for iframe in camera.capture_continuous(frame, format='bgr', use_video_port=True):
    image = iframe.array
    cv2.imshow('Frame in video',image)

    key = cv2.waitKey(1)&0xFF
    # clear stream
    frame.truncate(0)
    if key == ord('q'):
        break
cv2.destroyAllWindows()

camera.close()