import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def remove_the_blackborder(image):

    image = cv2.imread(image)      #读取图片
    img = cv2.medianBlur(image, 5) #中值滤波，去除黑色边际中可能含有的噪声干扰
    b = cv2.threshold(img, 3, 255, cv2.THRESH_BINARY) #调整裁剪效果
    binary_image = b[1]            #二值图--具有三通道
    binary_image = cv2.cvtColor(binary_image,cv2.COLOR_BGR2GRAY)
    # print(binary_image.shape)     #改为单通道
 
    edges_y, edges_x = np.where(binary_image==255) ##h, w
    bottom = min(edges_y)             
    top = max(edges_y) 
    height = top - bottom            
                                   
    left = min(edges_x)           
    right = max(edges_x)             
    height = top - bottom 
    width = right - left

    res_image = image[bottom:bottom+height, left:left+width]

    #plt.savefig(os.path.join("res_combine.jpg"))
    return res_image                                          
 
source_path = r"C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\case-cuhk_lib\img\right_top_save\origin"                               
save_path = r"C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\case-cuhk_lib\img\right_top"                                   
if not os.path.exists(save_path):
    os.mkdir(save_path)

for filename in os.listdir(source_path):
    if filename.endswith('.jpg'):
        img = remove_the_blackborder(os.path.join(source_path, filename))
        cv2.imwrite(os.path.join(save_path, filename), img)