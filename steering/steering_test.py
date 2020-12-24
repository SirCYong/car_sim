# -*- coding: utf-8 -*-
# create time    : 2020-12-24 14:30
# author  : CY
# file    : steering_test.py
# modify time:


def on_down(angle):
    if angle >= 45: info = '向下'
    else: info = '向上'
    print(f'{info}{angle}')


def left_right_camera(angle):
    if angle >= 90: info = '向右'
    else: info = '向左'
    print(f'{info}{angle}')


def left_right_car(angle):
    if angle >= 90: info = '向右'
    else: info = '向左'
    print(f'{info}{angle}')


def speed_car(car_status, speed='low'):
    """
    1 前进
    2 后退
    """
    info = '后退'
    if car_status == 1:
        IN1 = 0
        IN2 = 1
        info = '前进'
        pwm = speed
    else:
        IN1 = 1
        IN2 = 0
        pwm = speed
    print(f'{info}in1{IN1}in2{IN2}speed{pwm}')

