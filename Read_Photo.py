import cv2

frame=cv2.imread('lena.tiff')
src=cv2.imshow('photo',frame)
img_HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

src=cv2.imshow('HSV',img_HSV)
cv2.waitKey()