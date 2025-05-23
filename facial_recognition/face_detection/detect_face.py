import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
print("Camera opened")

while True:
	blah, img = cap.read()
	rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	faces = face_cascade.detectMultiScale(rgb, 1.1, 6)

	path = os.getcwd() + '/faces/'
	count = 1
	for x, y, w, h in faces:
		face = img[y:y+h, x:x+w] #slice the face from the image
		cv2.imwrite(path + 'face' + str(count) + '.jpg', face) #save the image
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 150), 5)
		cv2.putText(img, "id=" + str(count), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
		count+=1

	cv2.imshow('img', img)

	key = cv2.waitKey(30) & 0xff
	if key == 27:
		break

print("Camera closed")
cap.release()