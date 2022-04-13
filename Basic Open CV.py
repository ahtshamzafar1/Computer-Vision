import cv2
import numpy as np

# Import Image
'''''
img = cv2.imread("C:/Users/ahtis/OneDrive/Desktop/img.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)
'''''
#########################################################################################################################################

# Import Video
'''''
cap = cv2.VideoCapture("C:/Users/ahtis/OneDrive/Desktop/vid.mp4")
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    cv2.waitKey(1)
'''''
#################################################################################################################################

# Default Webcam Live Streaming
'''''
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    cv2.waitKey(1) # Delay in milliseconds 
'''''
#################################################################################################################################


# Basic Operations (Color Conversions, Image Blur, Edge Detector, Dilation, Erosion )
'''''
kernel = np.ones((5,5),np.uint8)

img = cv2.imread("C:/Users/ahtis/OneDrive/Desktop/img.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Other color conversions available in this function
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # Blur Image Function
imgCanny = cv2.Canny(img, 100,100) # Canny Edge Detector , 100 and 100 are thresholds.
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) # To increase line thickness
imgEroded = cv2.erode(imgDilation,kernel,iterations=2) # To distort line thickness

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilated Image",imgDilation)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)
'''''
#################################################################################################################################


# Resizing and Cropping
'''''
img = cv2.imread("C:/Users/ahtis/OneDrive/Desktop/img.jpg")
print (img.shape)

imgResize = cv2.resize(img,(400,150)) # Resize to:  Width = 400 , Height = 150
print (imgResize.shape)

imgCropped = img [0:300,0:500]  # Crop to:  Width = 0:500 , Height = 0:300
print (imgCropped.shape)

cv2.imshow("output",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)
'''''
#################################################################################################################################


# Shapes and Texts on image
'''''
img = np.zeros((512,512,3)) # Generate image of 512x512
img[:] = 255,0,0 # Make it blue
cv2.line(img,(0,0),(300,300),(0,255,0),3) # Draw line - Arguments (img,start pos, end pos, color, thickness)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # full diagonal line - Args (img,start, (img width/img height), color, thickness)
cv2.rectangle(img,(0,0),(250,350),(255,0,255),3) # Draw Rectangle from (0,0) to (250,350)
cv2.rectangle(img,(0,0),(250,350),(255,0,255),cv2.FILLED) # Filled Rectangle
cv2.circle(img,(400,50),30,(255,255,0),5) # Args (img, center point, radius, color, thickness)
cv2.putText(img,"TEXT",(300,200),cv2.FONT_HERSHEY_SIMPLEX,2,(150,0,0),2) # Args (img, text, start point, font, font size, color, thickness)


cv2.imshow("image", img)
cv2.waitKey(0)
'''''
#################################################################################################################################




