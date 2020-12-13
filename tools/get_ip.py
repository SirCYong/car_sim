# -*- coding: utf-8 -*-
# @create_time : 2020/12/12 2:04 上午
# @Author : CY
# @File : get_ip.py
import socket


def get_ip(error_num=3):
    """
    查询本机ip地址
    :return: ip
    """
    i = 0
    while 1:
        try:
            i += 1
            driver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            driver.connect(('8.8.8.8', 80))
            ip = driver.getsockname()[0]
            driver.close()
            break
        except Exception as e:
            print(e)
            print(f'error again {i} num')
            if i > error_num:
                raise Exception(e)
    return ip


if __name__ == '__main__':
    print(get_ip())

