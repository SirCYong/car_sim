# -*- coding: utf-8 -*-
# create time    : 2020-12-24 14:13
# author  : CY
# file    : car_sub_mqtt.py
# modify time:
import base64
import json
import time

import paho.mqtt.client as mqtt

from rtmp_video.rtmp_video_test import start_push_rtmp, stop_push_rtmp
from steering.steering_test import on_down, left_right_camera, status_speed_car, left_right_car, cat_status_stop


def on_connect(client_driver, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(client_driver, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    sub_data = json.loads(msg.payload.decode('utf-8'))
    print(sub_data)
    start_time = sub_data['time']
    end_time = time.time() - start_time
    print(end_time)
    if 'push_rtmp' in sub_data.keys():
        if sub_data['push_rtmp'] == 0:
            start_push_rtmp()
        else:
            stop_push_rtmp()
    if 'camera_up_down' in sub_data.keys():
        on_down(sub_data['camera_up_down']['angle'])

    if 'camera_left_right' in sub_data.keys():
        left_right_camera(sub_data['camera_left_right']['angle'])

    if 'car_up_down' in sub_data.keys():
        car_data = sub_data['car_up_down']
        car_status = car_data['car_status']
        speed = car_data['speed']
        status_speed_car(car_status=car_status, speed=speed)

    if 'car_left_right' in sub_data.keys():
        left_right_car(sub_data['car_left_right']['angle'])

    if 'cat_stop' in sub_data.keys():
        cat_status_stop()

    end_time = time.time() - start_time
    print(end_time)


if __name__ == '__main__':
    control_topic = 'control'
    client = mqtt.Client()
    client.username_pw_set(username='caoyong', password='admin123')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('192.168.22.70', 61883, 600)  # 600为keepalive的时间间隔
    client.subscribe(control_topic, qos=0)
    client.loop_forever()  # 保持连接
