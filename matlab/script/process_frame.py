import cv2
import os

def main():    
    data_path = "C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\case-cuhk_lib\\3\\"
    out_path = "C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\case-cuhk_lib\\3_out.mp4"
    fps = 29.97          # 视频帧率
    size = (5312, 2988) # 需要转为视频的图片的尺寸
    video = cv2.VideoWriter(out_path, -1, fps, size)
    
    # for i in range(500):
    #    image_path = data_path + "%d.jpg" % (i+1)
    #    print(image_path)
    #    img = cv2.imread(image_path)
    #    video.write(img)

    for i in range(2, 103630, 2):
        if i < 100:
            i = f"{i:03d}"
        else:
            i = str(i)
        image_path = data_path + i + '.jpg'
        print(image_path)
        img = cv2.imread(image_path)
        video.write(img)
    
    video.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()