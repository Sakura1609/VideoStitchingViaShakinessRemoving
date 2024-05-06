import os

for filename in os.listdir('./3'):
    try:
        image_number = int(filename.split('.')[0])  # 获取图片文件名中的编号部分
        if image_number % 2 != 0:  # 如果编号是奇数
            os.remove(os.path.join('./3/', filename))  # 删除该图片
            print(f"Deleted {filename}")
    except ValueError:
        print(f"Ignored {filename}, not a numbered image file.")
