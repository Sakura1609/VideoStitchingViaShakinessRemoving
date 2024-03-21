import cv2
import numpy as np
import os

from numba import jit

input_path = 'C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\\after_process\\5\\res\\'
output_path = 'C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\\after_process\\5\\out\\'

@jit
def process():
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    for file in os.listdir(input_path):
        print(file)
        img = cv2.imread(input_path + file)
        rows = img.shape[0]
        cols = img.shape[1]
        blank = np.zeros_like(img)
        # blank = np.zeros((4000,4000,3))
        #圆心定为图片中心
        center_x = int(rows / 2)
        center_y = int(cols / 2)
        #假设球的半径
        r = int(((rows**2+cols**2)**0.5)/2)+20
        #假设映射平面位于 z = r 处
        pz = r
        x, y = np.meshgrid(range(rows), range(cols))
        ox, oy = x, y
        x = x - center_x
        y = y - center_y
        z = np.sqrt(r*r - x*x - y*y)
        k = (pz - 2*r) / (z - 2*r)
        px = (k*x).astype(int) + center_x
        py = (k*y).astype(int) + center_y
        blank[px, py] = img[ox, oy]
        # for x in range(rows):
        #     ox = x
        #     x = x - center_x
        #     for y in range(cols):
        #         oy = y
        #         y = y - center_y
        #         z = (r*r - x*x - y*y)**0.5
        #         #假设光源点为(0,0,2r)
        #         k = (pz - 2*r)/(z - 2*r)
        #         px = int(k*x)
        #         py = int(k*y)
        #         px = px + center_x
        #         py = py + center_y
        cv2.imwrite(output_path + file,blank)

if __name__ == '__main__':
    process()