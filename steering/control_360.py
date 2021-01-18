# -*- coding: utf-8 -*-
# create time    : 2021-01-18 11:18
# author  : CY
# file    : control_360.py
# modify time:


import atexit
import RPi.GPIO as GPIO  # Introduce GPIO module
import time

atexit.register(GPIO.cleanup)
ServoPin = 27  # 角针 27
PWMFreq = 50  # PWM 脉宽调制信号频率

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ServoPin, GPIO.OUT)
pwm = GPIO.PWM(ServoPin, PWMFreq)  # Create a PWM object and set the frequency to 50
pwm.start(0)  # Start PWM and set the initial duty cycle to 0


def control_360(angle=None):
    try:
        while True:
            # direction = angle
            direction = float(input("请输入角度:"))
            if direction < 0 or direction > 360:
                print(f"取值范围在1~359，你输入的{direction}")
                continue

            duty = (1 / 36) * direction + 2.5
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.02)
    finally:
        pwm.stop()
        GPIO.cleanup()


if __name__ == '__main__':

    control_360()

