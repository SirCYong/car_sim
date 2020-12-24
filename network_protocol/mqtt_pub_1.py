# -*- coding: utf-8 -*-
# create time    : 2020-12-23 17:33
# author  : CY
# file    : mqtt_pub_1.py
# modify time:
import paho.mqtt.client as mqtt


def on_connect(client_driver, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(client_driver, userdata, msg):
    print(msg.topic + " " + str(msg.payload) + type(msg.payload))


if __name__ == '__main__':
    control_topic = 'control'
    client = mqtt.Client()
    client.username_pw_set(username='caoyong', password='admin123')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('192.168.22.70', 61883, 600)  # 600为keepalive的时间间隔
    push_new = {'0': 1}
    client.publish(control_topic, payload='vv', qos=0)
