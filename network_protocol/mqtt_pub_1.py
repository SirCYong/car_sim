# -*- coding: utf-8 -*-
# create time    : 2020-12-23 17:33
# author  : CY
# file    : mqtt_pub_1.py
# modify time:
import json
import time

import paho.mqtt.client as mqtt


if __name__ == '__main__':
    control_topic = 'control'
    client = mqtt.Client()
    client.username_pw_set(username='caoyong', password='admin123')
    client.connect('192.168.22.70', 61883, 600)  # 600为keepalive的时间间隔
    push_new = {'0': 1, 'time': time.time(),
                'push_rtmp': 0,
                'camera_up_down': {'angle': 45},
                'camera_left_right': {'angle': 90},
                'car_left_right': {'angle': 45},
                'car_up_down': {'car_status': 1, 'speed': 'high'},
                'cat_stop': 1
                }

    client.publish(control_topic, payload=json.dumps(push_new), qos=0)
