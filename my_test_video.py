# -*- coding: utf-8 -*-
# create time    : 2020-12-08 16:27
# author  : CY
# file    : my_test_video.py
# modify time:
from io import StringIO, BytesIO

import numpy as np
import cv2





def view_local_video():
    # cap = cv2.VideoCapture('test.rmvb')  # 参数为0时调用本地摄像头；url连接调取网络摄像头；文件地址获取本地视频
    cap = cv2.VideoCapture(0)
    while 1:
        ret, frame = cap.read()
        # 灰度化
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print('gray', gray)
        # frame = cv2.flip(frame, 1)
        cv2.imshow('frame', gray)

        # 普通图片
        cv2.imshow('frame', frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    view_local_video()
