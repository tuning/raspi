## Run Yolo3-tiny near realtime on Raspberry Pi

1. Raspberry Pi does not have a powerful GPU to enable fast ML inference. NNPACK acceleration using multicore CPU is probably the fastest possible way to go.

2. With NNPACK, Yolo3-tiny model can run at 1.7FPS on my Raspberry Pi 4B (Hardware Rev 1.1). You can even use the full Yolo3 model to detect objects either in a picture or in a live video stream (at ~0.2fps) with the 4GB Pi 4B model. You will get segmentaion error if you run out of memory.

3. A detailed guide can be found at https://github.com/zxzhaixiang/darknet-nnpack/tree/yolov3#step-3-test-with-yolov3-tiny No surprises.

4. When compiling, use the Makefile that I provide here.

5. (From Joseph Redmon's official Yolo website) In command line, use the following command to run Yolo3-tiny on your picture:./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights yourpicture.jpg

6. (From Joseph Redmon's official Yolo website) In command line, use the following command to run a live demo:./darknet detector demo cfg/coco.data cfg/yolov3-tiny.cfg yolov3-tiny.weights

7. Make sure to checkout Joseph Redmon's resume. Made my day. Likely to make yours too XD. Too bad he is quitting the CV community.