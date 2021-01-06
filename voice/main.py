# -*- coding: utf-8 -*-
# create time    : 2020-12-30 15:55
# author  : CY
# file    : main.py
# modify time:


import sys
import time
import argparse

from voice.voice_client import VoiceClient
from voice.voice_server import VoiceServer

parser = argparse.ArgumentParser()

parser.add_argument('--host', type=str, default='127.0.0.1')
parser.add_argument('--port', type=int, default=10087)
parser.add_argument('--level', type=int, default=1)
parser.add_argument('-v', '--version', type=int, default=4)
print('par')
print(parser)

args = parser.parse_args()

IP = args.host
PORT = args.port
VERSION = args.version
LEVEL = args.level
print('ar')
print(args)

if __name__ == '__main__':
    vclient = VoiceClient(IP, PORT, VERSION)
    vserver = VoiceServer(PORT, VERSION)

    vclient.start()
    time.sleep(1)    # make delay to start server
    vserver.start()
    while True:
        time.sleep(1)
        if not vserver.is_alive() or not vclient.is_alive():
            print("Video connection lost...")
            sys.exit(0)