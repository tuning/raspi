#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:32:53 2020

@author: tutu

Example: Preview and capture images using PiCamera
"""

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 0
camera.resolution = (480,320)
camera.framerate = 25
camera.annotate_text = "copyright @tutu"
camera.brightness = 60
camera.image_effect = "none"
camera.exposure_mode = "auto"
camera.awb_mode = "auto"

# capture still image
camera.start_preview(alpha=255)
sleep(5)
camera.capture('../pictures/basic.jpg')
camera.stop_preview()

# capture video
camera.start_preview(alpha=255)
sleep(5)
camera.start_recording('../pictures/basic.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()

# release camera resources
camera.close()