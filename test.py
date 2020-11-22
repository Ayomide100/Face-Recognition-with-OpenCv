import cv2
import numpy as numpy


cap = cv2.VideoCapture(0)

while(True):
	rect, frame = cap.read()
	cv2.imshow('frame', frame)
	if cv2.Waitkey


cap.release()
cv2.destroyAllWindows()