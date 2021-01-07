# -*- coding: utf-8 -*-
# create time    : 2020-12-07 17:55
# author  : CY
# file    : my_test_voice.py
# modify time:
import wave
import os
import pyaudio

input_filename = "input.wav"               # 麦克风采集的语音输入
input_filepath = os.getcwd()              # 输入文件的path
in_path = os.sep.join([input_filepath, input_filename])

print(in_path)


def get_audio(filepath):
    # aa = str(input("是否开始录音？   （是/否）"))
    aa = '是'
    if aa == str("是"):
        CHUNK = 256
        FORMAT = pyaudio.paInt16
        CHANNELS = 1                # 声道数
        RATE = 11025                # 采样率
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = filepath
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("*"*10, "开始录音：请在5秒内输入语音")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("*"*10, "录音结束\n")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        # wf.writeframes(frames)
        wf.close()
    elif aa == str("否"):
        exit()
    else:
        print("无效输入，请重新选择")


def read_voice(file_path):
    # define stream chunk
    chunk = 1024

    # open a wav format music
    f = wave.open(file_path, "rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # read data
    data = f.readframes(chunk)
    print(data)

    # paly stream
    while len(data) != 0:
        stream.write(data)
        data = f.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()
    f.close()


if __name__ == '__main__':
    # get_audio(in_path)
    read_voice(in_path)
