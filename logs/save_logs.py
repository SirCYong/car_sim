# -*- coding: utf-8 -*-
# create time    : 2021-01-06 9:49
# author  : CY
# file    : save_logs.py
# modify time:


import logging
import os


def save_log(filename='logger', level=1):
    """

    :param level: 1 debug 2 info 3 warm 4
    :param filename: log 名称
    :return:
    """
    filename = f"{filename}.log"
    log_path = os.path.dirname(os.path.realpath(__file__))
    print(log_path)
    path_file = os.sep.join([log_path, filename])

    if get_file_size(path_file, filename) > 2:
        clear_log_file(file_path=path_file)

    if level == 1: level = logging.DEBUG
    elif level == 2: level = logging.INFO
    elif level == 3: level = logging.WARN
    elif level == 4: level = logging.ERROR
    elif level == 5: level = logging.CRITICAL
    else: level = logging.DEBUG
    logging.basicConfig(filename=path_file, level=level)
    return logging


def get_file_size(file_path, file_name):
    """

    :param file_path:  文件路径
    :param file_name:  只是为了显示log 文件 名称
    :return:
    """
    """获取文件大小"""
    folder = os.path.exists(file_path)
    if not folder:
        new_file = open(file_path, 'w')
        new_file.close()
    file_size = os.path.getsize(file_path)
    file_size = file_size/float(1024*1024)
    print(f'{file_name} 文件大小{round(file_size, 2)}m')
    return round(file_size, 2)


def clear_log_file(file_name=None, file_path=None):
    """把log文件置为空"""
    if file_name is None and file_path is None:
        print("file_name file_path 二选一，必填")
    else:
        if file_name is not None:
            log_path = os.path.dirname(os.path.realpath(__file__))
            path_file = os.sep.join([log_path, f'{file_name}.log'])
        else:
            path_file = file_path
        try:
            with open(path_file, "r+") as f:
                f.truncate()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    log = save_log(filename='kill_driver')
    log.debug('debug info')

