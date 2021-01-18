# -*- coding: utf-8 -*-
# @create_time : 2020/12/20 2:17 上午
# @Author : CY
# @File : control_steering.py

from time import sleep
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def set_servo_angle(foot, angle, max_angle=180):
    """
    控制舵机
    servo 脚针
    angle 角度
    max_angle 舵机的最大角度 默认180
    17 最小值是68 最大值是179"""
    GPIO.setup(foot, GPIO.OUT)
    pwm = GPIO.PWM(foot, 50)
    pwm.start(8)
    if max_angle == 180: duty_cycle = angle / 18. + 3.
    elif max_angle == 360: duty_cycle = (1 / 36) * angle + 2.5
    else: raise Exception(f"最大角度仅支持180与360，你的最大角度{max_angle}")
    pwm.ChangeDutyCycle(duty_cycle)
    if max_angle == 180: sleep(0.3)
    else: sleep(0.02)
    pwm.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    input_foot = int(sys.argv[1])
    input_angle = int(sys.argv[2])
    if len(sys.argv) == 4:
        input_max_angle = int(sys.argv[3])
    else:
        input_max_angle = 180
    set_servo_angle(input_foot, input_angle)

