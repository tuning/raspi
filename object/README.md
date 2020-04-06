## Object detection

Use YoloV3-tiny for object detection and tracking.

- Command line interface

	- To apply it to a photo, run "bash detPhoto.sh" in command line, when prompted, input the path for your photo file *RELATIVE to darknet-nnpack*. When finished, press CTRL+C to quit.

	- To apply it to live video stream, run "bash detVideo.sh" in command line. When finished, press ESC to quit.

- If you want to wrap it into Python, checkout the rpi_record.py and rpi_video.py in this repo: https://github.com/zxzhaixiang/darknet-nnpack/tree/yolov3#step-3-test-with-yolov3-tiny