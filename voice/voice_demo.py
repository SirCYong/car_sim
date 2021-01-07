# -*- coding: utf-8 -*-
# create time    : 2020-12-30 10:39
# author  : CY
# file    : voice_demo.py
# modify time:
from voice.voice_client import VoiceClient


def start_voice_demo():
    print('语音功能已开启')
    VoiceClient()


def stop_voice_demo():
    print('语音功能已关闭')
