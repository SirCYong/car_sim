# -*- coding: utf-8 -*-
# @create_time : 2020/12/12 2:55 下午
# @Author : CY
# @File : rtmp_video.py

'''

python3

opencv

ffmpeg

rtmp 推流视频直播pipe:: Invalid argumentb

'''

import cv2

import subprocess

import shlex


# ffmpeg 推流

class FfmpegRemp(object):

    def __init__(self, rtmpfile, videoid):

        self.rtmpUrl = "rtmp://127.0.0.1:1935/" + rtmpfile

        self.video_stream_path = videoid

        self.WIDTH = 640

        self.HEIGHT = 420

        self.FPS = 30.0

        self.stat = True

    def open_opencv(self):

        cap = cv2.VideoCapture(0)

        # 设置摄像头设备分辨率

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.WIDTH)

        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.HEIGHT)

        # 设置摄像头设备帧率,如不指定,默认600

        cap.set(cv2.CAP_PROP_FPS, self.FPS)

        # 解决延迟

        cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

        return cap

    def open_ffmpeg(self):

        cap = self.open_opencv()

        fps = int(cap.get(cv2.CAP_PROP_FPS))

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # ffmpeg command

        command = ['ffmpeg',

                   '-y',
                   '-v', '24',

                   '-f', 'rawvideo',

                   '-vcodec', 'rawvideo',

                   '-pix_fmt', 'bgr24',

                   '-s', "{}x{}".format(width, height),

                   '-i', '-',

                   '-c:v', 'libx264',

                   '-pix_fmt', 'yuv420p',

                   '-preset', 'ultrafast',

                   '-f', 'rtsp',

                   self.rtmpUrl]

        # print(command)

        # 管道配置

        # self.p = sp.Popen(command, stdin=sp.PIPE, shell=True)

        p = subprocess.Popen(command, stdin=subprocess.PIPE)

        # read webcamera

        print('is_open', cap.isOpened())

        while (cap.isOpened()):

            ret, frame = cap.read()

            if not ret:

                print("Opening camera is failed")

                break

            elif not self.stat:

                p.kill()

                print("停止推流")

                break

            try: p.stdin.write(frame.tostring())
            except Exception as e: print(e)

    # 关闭直播

    def close_ffmpeg(self):

        self.stat = False

        self.open_ffmpeg()


if __name__ == "__main__":
    # run_opencv_camera()

    fr = FfmpegRemp("Live003", 0)

    fr.open_ffmpeg()
