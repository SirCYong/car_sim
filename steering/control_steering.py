# -*- coding: utf-8 -*-
# @create_time : 2020/12/20 2:17 上午
# @Author : CY
# @File : control_steering.py

from time import sleep
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def set_servo_angle(foot, angle):
    """
    控制舵机
    servo 脚针
    angle 角度
    17 最小值是68 最大值是179"""
    GPIO.setup(foot, GPIO.OUT)
    pwm = GPIO.PWM(foot, 50)
    pwm.start(8)
    duty_cycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(duty_cycle)
    sleep(0.3)
    pwm.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    input_foot = int(sys.argv[1])
    input_angle = int(sys.argv[2])
    set_servo_angle(input_foot, input_angle)

