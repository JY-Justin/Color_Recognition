import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow("RGB", 1)
cv2.namedWindow("HSV", 1)
cv2.namedWindow("MASK", 1)
cv2.namedWindow("target", 1)

while True:
    ret,frame = cap.read() 
    # frame = cv2.flip(frame, 1)
    image1 = cv2.putText(frame, 'Press esc to exit', (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255),
                         thickness=1, lineType=1)

    kernel_3 = np.ones((3, 3), np.uint8)  # 3x3的卷积核
    if frame is not None:
        HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 把BGR图像转换为HSV格式
        Lower = np.array([20, 20, 20])  # 要识别颜色的下限
        Upper = np.array([30, 255, 255])  # 要识别的颜色的上限

        # mask是把HSV图片中在颜色范围内的区域变成白色，其他区域变成黑色
        mask = cv2.inRange(HSV, Lower, Upper)

        # 卷积进行滤波
        erosion = cv2.erode(mask, kernel_3, iterations=1)
        erosion = cv2.erode(erosion, kernel_3, iterations=1)
        dilation = cv2.dilate(erosion, kernel_3, iterations=1)
        dilation = cv2.dilate(dilation, kernel_3, iterations=1)

        # target是把原图中的非目标颜色区域去掉剩下的图像
        target = cv2.bitwise_and(frame, frame, mask=dilation)

        # 变成二值图像放在binary中
        ret, binary = cv2.threshold(dilation, 127, 255, cv2.THRESH_BINARY)
        binary, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        p = 0
        for i in contours:  # 遍历所有的轮廓
            x, y, w, h = cv2.boundingRect(i)  # 将轮廓分解为识别对象的左上角坐标和宽、高
            # 在图像上画上矩形（图片、左上角坐标、右下角坐标、颜色、线条宽度）
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255,), 3)
    cv2.imshow('RGB', frame)
    cv2.imshow('HSV', HSV)
    cv2.imshow('MASK', mask)
    cv2.imshow('target', target)
    key = cv2.waitKey(3)
    if key == 27:
        break
