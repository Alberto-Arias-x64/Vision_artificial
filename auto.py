import cv2
import numpy as np 

region=[(275,270),(400,100),(580,270)]

def region_de_interes(img,vertices):
	mascara=np.zeros_like(img)
	#canal=img.shape[2]
	match=(255,)#*canal
	cv2.fillPoly(mascara,vertices,match)
	enmascarado=cv2.bitwise_and(img,mascara)
	return enmascarado

cap=cv2.VideoCapture("E:/Nueva carpeta/truck.mp4")
while cap.isOpened():

	ret,frame2=cap.read()
	imgc=cv2.resize(frame2,(800,400))
	img=cv2.cvtColor(imgc,cv2.COLOR_BGR2GRAY)
	blur=cv2.blur(img,(3,3))
	edges=cv2.Canny(blur,80,150,apertureSize=3)
	img=region_de_interes(edges,np.array([region],np.int32))
	
	lineas=cv2.HoughLinesP(img,1,np.pi/180,100,minLineLength=30,maxLineGap=10)
	try:
		for line in lineas:
		    x1,y1,x2,y2 = line[0]
		    cv2.line(imgc,(x1,y1),(x2,y2),(0,255,0),2)
		cv2.imshow('image', imgc)
	except: cv2.imshow('image', imgc)
	if cv2.waitKey(1) == 27:break
cap.release()
cv2.destroyAllWindows()