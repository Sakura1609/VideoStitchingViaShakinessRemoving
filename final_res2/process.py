import cv2

# 视频文件和对应的名称
videos = [
    {'file': 'l.mp4', 'name': 'Left'},
    {'file': 'case17-r.mp4', 'name': 'Right'},
    {'file': 'output.mp4', 'name': 'Blend'}
]

# 打开视频文件
cap = [cv2.VideoCapture(video['file']) for video in videos]

# 获取视频尺寸
frame_width = int(cap[0].get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap[0].get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建输出窗口
cv2.namedWindow('Multi Video Display', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Multi Video Display', frame_width * len(videos), frame_height)

while True:
    frames = []
    # 读取每个视频的帧
    for i, video_cap in enumerate(cap):
        ret, frame = video_cap.read()
        if not ret:  # 如果视频结束，重新打开视频以实现循环播放
            cap[i].release()
            cap[i] = cv2.VideoCapture(videos[i]['file'])
            _, frame = cap[i].read()
        # 在帧上方添加名称
        cv2.putText(frame, videos[i]['name'], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        frames.append(frame)
    
    # 拼接多个视频帧
    display_frame = cv2.hconcat(frames)

    # 显示拼接后的帧
    cv2.imshow('Multi Video Display', display_frame)

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
for video_cap in cap:
    video_cap.release()
cv2.destroyAllWindows()
