from PIL import Image
import os

def split_image(image_path, lp, rp):
    # 打开图片
    for img in os.listdir(image_path):
        original_image = Image.open(os.path.join(image_path, img))
        
        # 获取图片的宽度和高度
        width, height = original_image.size
        
        # 计算分割位置
        split_position = width // 2
        
        # 分割图片
        left_image = original_image.crop((0, 0, split_position, height))
        right_image = original_image.crop((split_position, 0, width, height))
        
        # 保存分割后的图片
        if os.path.exists(lp) == False:
            os.mkdir(lp)
        left_image.save(os.path.join(left_path, img))
        if os.path.exists(rp) == False:
            os.mkdir(rp)
        right_image.save(os.path.join(right_path, img))

# 调用函数并传入图片路径

left_path = r"C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\case-cuhk_lib\cut2half\left_left"
right_path = r"C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\case-cuhk_lib\cut2half\left_right"
path = r"C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\case-cuhk_lib\cut2half\left"
split_image(path, left_path, right_path)
