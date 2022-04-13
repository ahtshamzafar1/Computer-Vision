import cv2


#img = cv2.imread("C:/Users/ahtis/OneDrive/Desktop/img.jpg")
#cv2.imshow("output",img)
#cv2.waitKey(0)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    cv2.waitKey(1)
