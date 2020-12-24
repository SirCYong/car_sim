# -*- coding: utf-8 -*-
# create time    : 2020-12-23 17:34
# author  : CY
# file    : mqtt_sub_1.py
# modify time:

import paho.mqtt.client as mqtt


def on_connect(client_driver, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(client_driver, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


if __name__ == '__main__':
    control_topic = 'control'
    client = mqtt.Client()
    client.username_pw_set(username='caoyong', password='admin123')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('192.168.22.70', 61883, 600)  # 600为keepalive的时间间隔
    client.subscribe(control_topic, qos=0)
    client.loop_forever()  # 保持连接

