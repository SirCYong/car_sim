# -*- coding: utf-8 -*-
# create time    : 2020-12-22 10:36
# author  : CY
# file    : rtmp_push_video.py
# modify time:
import os
import subprocess
import sys
from time import sleep


def rtmp_push_video():
    """rtmp 推流"""
    rtmp_url = 'rtmp://192.168.22.70:1935/live/home'
    now_platform = sys.platform
    if now_platform in 'win32':
        command = f'ffmpeg -f dshow -i video="Integrated Webcam"  -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f flv {rtmp_url}'
    elif now_platform == 'linux':
        command = 'ffmpeg -ss 0 -i /dev/video0  -f flv rtmp://192.168.1.212:1935/live/home'
    else:
        raise Exception(f'not support {now_platform}')
    p = subprocess.Popen(command, shell=True)
    # print(p.communicate())
    sleep(30)


def stop_rtmp_push():
    now_platform = sys.platform
    try:
        if now_platform in 'win32':
            cmd = 'taskkill /F /IM ffmpeg.exe'
        elif now_platform == 'linux':
            cmd = ''
        else: raise Exception(f'not support {now_platform}')
        p = os.popen(cmd)
        print(p.read())
        print('ffmpeg服务关闭')
    except Exception as e:
        print(e)


if __name__ == '__main__':

    print(sys.platform)
    rtmp_push_video()

