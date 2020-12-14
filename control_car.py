# -*- coding: utf-8 -*-
# create time    : 2020-12-14 15:23
# author  : CY
# file    : control_car.py
# modify time:


import RPi.GPIO as GPIO
import time  # 导入库

# 这些是各个引脚的接口
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13
# GPIO初始化模式
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# GPIO初始化状态
def motor_init():
    # pwm_ENA and pwm_ENB 是用来控制小车速度的
    global pwm_ENA
    global pwm_ENB
    global delaytime  # delaytime 可以用来控制小车的运动时间
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    # 设置pwm频率
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    # pwm启动
    pwm_ENA.start(0)
    pwm_ENB.start(0)


#############################################################################
# 前面已经将小车的引脚初始化完成了，现在所需要的就是控制引脚的电流来控制小车的运动
# GPIO.output() 可以用来控制电流，pwm.ChangeDutyCycle()是用来控制频率的,间接用来控制车速
# 我的小车的IN1和IN2是一对，IN3和IN4是一对 当1是HIGH的时候左边前进,2是HIGH的时候左边后退
# 1和2，3和4 只能是HIGH和LOW 一对的 不能是两个都是HIGH 或者 LOW
# 可能每个人的车都不一样吧，大体套路都是一样的
############################################################################
# 前进
def run(delaytime):
    GPIO.output(IN1, GPIO.HIGH)  # setting GPIO
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)  # setting speed
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)  # setting delaytime


# 左转
def left(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(40)
    pwm_ENB.ChangeDutyCycle(40)
    time.sleep(delaytime)


# 原地左转
def spin_left(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(10)
    pwm_ENB.ChangeDutyCycle(40)
    time.sleep(delaytime)


def right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)


# 原地右转
def spin_right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)


# 停车
def brake(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)


# 后退
def back(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)
# 前面几个函数分别是用来控制小车运动的 可以通过一系列检测或者控制来使用上面
# 的函数，从而达到与小车的信息交互



