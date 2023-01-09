# ComputerVision
 
# Basic Open CV
- Importing videos
- Default Webcam Live Streaming
- Basic Operations (Color Conversions, Image Blur, Edge Detector, Dilation, Erosion )
- Resizing and Cropping
- Shapes and Texts on image

# Vertical Edge and Line Detector
Numpy Based Edge Detector using edge detection kernels. Implemented from scratch using only numpy for processing. Outputs higher number in case of detected edges, and outputs lower number in case no edges (Number itself depends on amount of edges detected). 
 
# Object Detection-YOLO V3
Object detection is one of the most researched and utilized topic in Applied AI real world problems. 
YOLO V3 Provides a DarkNet Backend framework to detect objects in real time, it can go as fast as 30fps of real time object detection and classification, This make YOLO V3 one of the widely used models. 
The Notebook contains a fully functional YOLOV3 Transfer Learning Model, whcih can be tuned for your specific purpose accordingly. 

# YOLOv7
YOLO v7 is the latest version of the YOLO object detection system. It is a fast and accurate object detection system that can be used for a variety of applications, including self-driving cars, security systems, and robotics.
One of the key features of YOLO is its ability to process images and videos in real-time, making it suitable for use in applications where speed is important. YOLO v7 uses a single convolutional neural network (CNN) to detect objects in an image or video, and can predict the class and location of multiple objects in a single pass.
This code extracts detected object from the video/image and generates cropped output video/image file with only the object and black pixels around it. 

# Angle Based Pose Recognition
Angle-based pose recognition refers to the process of estimating the pose (i.e., the position and orientation) of an object or a person from a single image or video frame by determining the angles between different parts of the object or person. This is typically done using computer vision techniques and machine learning algorithms.
This project provides one possible vision framework based pose recognition, using pose estimation first and then calculating angles. 

# Mediapipe pose estimation
MediaPipe is an open-source framework developed by Google that provides a high-level interface for creating and deploying machine learning models for a wide range of applications, including pose estimation.
Pose estimation using MediaPipe involves designing and training a machine learning model to predict the pose of an object or person from an image or video frame. This is typically done using a combination of computer vision techniques and machine learning algorithms.
This code only estimates the pose, but pose recognition can be done afterwards using angle based pose estimation or passing the pose coordinates to an ML algorithm for training. 

# Coin Detection, Segmentation and Counting
A simple edge detector based code for detection and segmentation of coins. The segmented countours can also be used to count the number of coins inside the frame. 

# Video file Type Converter 
Python script to convert between MP4 and AVI video file formats for optimised compression in a particular use case. 
