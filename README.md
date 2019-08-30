# 使用opencv对图片进行特定颜色识别

使用环境win10x64
使用框架python+opencv

文件1：read_photo.py用于读取图片进行hsv色域转换  
文件2：test_img.py用于对图片特定颜色识别，这里我识别的是黄色  
文件3：test_video.py这里开启本地摄像头对视频流进行颜色识别，也可以对本地视频进行识别  
## 主要知识：  
rgb色域到hsv色域的转换，HSV是一种比较直观的颜色模型，对于人类分辨颜色更友好。  
这个模型中颜色的参数分别是：色调（H, Hue），饱和度（S,Saturation），明度（V, Value）。 
### HSV色彩空间图为：
![](https://github.com/omega-Lee/Color_Recognition/blob/master/hsv.jpg)

## 实验效果：  
![](https://github.com/omega-Lee/Color_Recognition/blob/master/Img.png)
