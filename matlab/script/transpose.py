from PIL import Image
import os
import os.path
import cv2 as cv

rootdir = r'C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\case-cuhk_lib\img\right_top_save\origin'  # 指明被遍历的文件夹
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)

        
        im = Image.open(currentPath)
        # img = cv.imread(currentPath)
        #进行上下颠倒
        # out = im.transpose(Image.FLIP_TOP_BOTTOM)
        # #进行左右颠倒
        # out =out.transpose(Image.FLIP_LEFT_RIGHT)
        # # 进行旋转90
        out = im.transpose(Image.ROTATE_90)
        # # 进行旋转180
        # out = im.transpose(Image.ROTATE_180)
        # # 进行旋转270
        # out = im.transpose(Image.ROTATE_270)
        
        # #将图片重新设置尺寸
        # img= im.resize((720, 720))
        
        # im = cv.resize(img, (720, 720))
        # img = cv.copyMakeBorder(im, 200, 200, 200, 200, cv.BORDER_CONSTANT, value=[0, 0, 0])
        # # 指定旋转角度（逆时针为正方向）
        # angle = 45

        # # 获取图像的中心点
        # height, width = img.shape[:2]
        # center = (width // 2, height // 2)

        # # 计算旋转矩阵
        # rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)

        # # 使用仿射变换旋转图像
        # out = cv.warpAffine(img, rotation_matrix, (width, height))
        # # out = out.rotate(45)
        # # out = out.transpose(Image.ROTATE_90)
        # # out = out.resize((720, 368))
        newname = r"C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\case-cuhk_lib\img\right_top" + '\\' + filename
        # cv.imwrite(newname, out)
        out.save(newname)