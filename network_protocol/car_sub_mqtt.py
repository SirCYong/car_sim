# -*- coding: utf-8 -*-
# create time    : 2020-12-24 14:13
# author  : CY
# file    : car_sub_mqtt.py
# modify time:
import json
import threading
import time
import paho.mqtt.client as mqtt
from logs.save_logs import save_log
from rtmp_video.rtmp_video_test import start_push_rtmp, stop_push_rtmp
from steering.steering_test import on_down, left_right_camera, status_speed_car, left_right_car, cat_status_stop
from tools.base_tools import get_now
from voice.voice_demo import start_voice_demo, stop_voice_demo

logger = save_log(filename='open_door')


class MqttSub(object):
    def __init__(self, topic):
        self.client = mqtt.Client()
        self.topic = topic

        self.username = 'caoyong'
        self.password = 'admin123'
        self.url = '192.168.22.70'
        self.port = '61883'
        self.keep_live = 600

    def on_connect(self, client_driver, userdata, flags, rc):
        logger.info("Connected with result code: " + str(rc))
        print("Connected with result code: " + str(rc))
        print(rc)
        if rc == 0:
            client_driver.subscribe(self.topic, qos=0)

    @classmethod
    def on_message(cls, client_driver, userdata, msg):
        logger.info(f'{msg.topic} {msg.payload}')
        print(f'{msg.topic} {msg.payload}')
        sub_data = json.loads(msg.payload.decode('utf-8'))
        logger.info(f'{get_now()}{sub_data}')
        print(sub_data)
        start_time = sub_data['time']
        end_time = time.time() - start_time
        print('消息从发送到接收的时间', end_time)
        logger.info(f'{get_now()}消息从发送到接收的时间{end_time}')

        if 'push_rtmp' in sub_data.keys():
            if sub_data['push_rtmp'] == 0:
                thread = threading.Thread(target=start_push_rtmp)
            else:
                thread = threading.Thread(target=stop_push_rtmp)
            thread.start()
        if 'voice' in sub_data.keys():
            if sub_data['push_rtmp'] == 0:
                thread = threading.Thread(target=start_voice_demo)
            else:
                thread = threading.Thread(target=stop_voice_demo)
            thread.start()
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
        logger.info(f'{get_now()}最终时间{end_time}')

    def mqtt_sub_main(self):
        self.client.username_pw_set(username=self.username, password=self.password)
        self.client.connect(self.url, self.port, self.keep_live)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.loop_forever(retry_first_connection=True)  # 保持连接


if __name__ == '__main__':
    control_topic = 'control'
    MqttSub(topic=control_topic).mqtt_sub_main()
