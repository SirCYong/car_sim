# -*- coding: utf-8 -*-
# create time    : 2020-12-14 15:53
# author  : CY
# file    : read_server_video.py
# modify time:


import cv2
import socket
import time
from PIL import Image
from io import BytesIO
import numpy as np

# 注意IP地址和端口号与前面的程序中的保持一致
HOST, PORT = "192.168.0.104", 9999
# 连接到服务器
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    msg = sock.recv(1024 * 1024)
    if not msg:
        break
    buf = BytesIO(msg)
    buf.seek(0)
    try:
        pi = Image.open(buf)  # 使用PIL读取jpeg图像数据

        img_array = np.array(pi)
        if img_array.dtype == object:
            try: img_array = img_array.astype(np.uint8)
            except Exception as e: print(e)
        print(img_array.dtype)

        try: img = cv2.cvtColor(np.asarray(img_array), cv2.COLOR_RGB2BGR)
        except Exception as e: print(e)

        cv2.imshow("camera", img)  # 实时显示
    except(OSError, NameError):
        print('OSError')

    if cv2.waitKey(10) == ord('q'):
        break

sock.close()
cv2.destroyAllWindows()
