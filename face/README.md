## Face recognition

### Directory structures

- pictures: save captured generic pictures

- faces: save detected faces to train face-recognition model

- etc: misc files necessary for various models

- cameraIO: basic camera functions with raspi

### scripts:

- faceDetection: demo of face detection that also saves faces (300*300 pixels) to the "faces" dir.

- faceRecognition: use the faces saved in "faces" dir to train a face recognition model

- faceDetAndRec: use the model to identify person faces in live camera stream