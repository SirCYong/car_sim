# -*- coding: utf-8 -*-
# @create_time : 2020/12/20 2:17 上午
# @Author : CY
# @File : control_steering.py

from time import sleep
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def set_servo_angle(servo, angle):
    """控制舵机"""
    GPIO.setup(servo, GPIO.OUT)
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    duty_cycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(duty_cycle)
    sleep(0.3)
    pwm.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    servo = int(sys.argv[1])
    set_servo_angle(servo, int(sys.argv[2]))

