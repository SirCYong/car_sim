# -*- coding: utf-8 -*-
# @create_time : 2020/12/13 1:09 上午
# @Author : CY
# @File : new_rtmp_video.py

import queue
import threading
import cv2
import subprocess as sp

# 自行设置,url为推送的服务器地址
rtmpUrl = "rtmp://127.0.0.1:1935/live/test"
cap = cv2.VideoCapture(0)

fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# ffmpeg command
command = ['ffmpeg',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-r', str(fps),
           '-i', '-',
           '-c:v', 'libx264',
           '-pix_fmt', 'yuv420p',
           '-preset', 'ultrafast',
           '-f', 'flv',
           rtmpUrl]

# 设置管道
p = sp.Popen(command, stdin=sp.PIPE)
while True:
    ret, frame = cap.read()
    try:
        p.stdin.write(frame.tostring())
    except Exception as e: print(e)

