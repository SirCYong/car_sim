# -*- coding: utf-8 -*-
# create time    : 2021-01-18 11:18
# author  : CY
# file    : control_360.py
# modify time:


import atexit
import RPi.GPIO as GPIO  # Introduce GPIO module
import time
import numpy as np
import math

atexit.register(GPIO.cleanup)
ServoPin = 21
PWMFreq = 50  # PWM signal frequency

GPIO.setmode(GPIO.BCM)  # Use BCM numbering method
GPIO.setup(ServoPin, GPIO.OUT)  # Set GPIO19 to output mode
pwm = GPIO.PWM(ServoPin, PWMFreq)  # Create a PWM object and set the frequency to 50
pwm.start(0)  # Start PWM and set the initial duty cycle to 0


# Servo that can control 300 degree rotation
def Control_300(angle=None):
    try:
        while True:
            # ~ # Waiting to enter an angle from 0 to 300
            # ~ direction = angle
            direction = float(input("Please enter the moving angle:"))
            if direction < 0 or direction > 300:
                print("Please enter the correct angle")
                continue

            duty = (1 / 30) * direction + 2.5  # Convert angle to duty cycle
            pwm.ChangeDutyCycle(duty)  # Change the PWM duty cycle
            time.sleep(0.02)
    finally:
        pwm.stop()  # Stop PWM
        GPIO.cleanup()  # Clean and release GPIO resources, reset GPIO


# Can control 360 degree rotating servo
def Control_360(angle=None):
    try:
        while True:
            # ~ # Waiting to enter an angle from 0 to 300
            # ~ direction = angle
            direction = float(input("Please enter the moving angle:"))
            if direction < 0 or direction > 360:
                print("Please enter the correct angle")
                continue

            duty = (1 / 36) * direction + 2.5  # Convert angle to duty cycle
            pwm.ChangeDutyCycle(duty)  # Change the PWM duty cycle
            time.sleep(0.02)
    finally:
        pwm.stop()  # Stop PWM
        GPIO.cleanup()  # Clean and release GPIO resources, reset GPIO


# Uncontrollable 360 ​​degree rotation
def UnControl_360(angle=None):
    try:
        # Wait to enter an angle from 0 to 300
        direction = angle
        # ~ direction = float(input("Please enter the moving angle: "))
        if direction < 0 or direction > 360:
            print("Please enter the correct angle")
        duty = (1 / 30) * direction + 2.5  # Convert angle to duty cycle
        pwm.ChangeDutyCycle(duty)  # Change the PWM duty cycle
        time.sleep(0.02)

    finally:
        pwm.stop()  # Stop PWM
        GPIO.cleanup()  # Clean and release GPIO resources, reset GPIO


if __name__ == '__main__':

    Control_360()
    # ~ img = grap_photo()
    # ~ data = SMD2(img)
    # ~ print(data)
    # ~ if data>10000:
    # ~ Control_300(200)
    # ~ else:
    # ~ Control_300(10)
