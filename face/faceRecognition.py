#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:41:02 2020

@author: tutu

Here we use the acquired face photo crops to train a vanilla face recognition
system.
"""
import os
import cv2
import numpy as np

faceDir = './faces/train/'
personDirs = os.listdir(faceDir)
faceSize = (300,300)
faceArray = []
idArray = []
faceRecognizer = cv2.face.createLBPHFaceRecognizer()
faceCounter = 0

for personDir in personDirs:
    personId = int(personDir[-1])
    personPath = os.path.join(faceDir,personDir)
    for personFaceFile in os.listdir(personPath):
        personFaceFilePath = os.path.join(personPath, personFaceFile)
        if personFaceFilePath.endswith('jpg')|personFaceFilePath.endswith('png'):
            if personFaceFile[0]!='.': # to avoid hidden metadata files
                # read image as grayscale with second parameter being 0
                imageArray = cv2.imread(personFaceFilePath,0)
                faceArray.append(imageArray)
                idArray.append(personId)
                faceCounter += 1

print('Finished loading '+str(faceCounter)+' faces. Start training...\n')
# face recognizer expects numpy array as labels
faceRecognizer.train(faceArray, np.array(idArray))
faceRecognizer.save('./faces/model/faceRecModel.yml')
print('Finished training.')
