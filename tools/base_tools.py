# -*- coding: utf-8 -*-
# create time    : 2021-01-06 9:47
# author  : CY
# file    : base_tools.py
# modify time:
import datetime


def get_now(day=0, hours=0, minutes=0, time_type='%Y-%m-%d %H:%M:%S'):
    """
    当前日期 时间
    '%Y-%m-%d'
    '%Y-%m-%d %H:%M:%S.%f'
    """
    now_time = (datetime.datetime.now() + datetime.timedelta(days=+day, hours=+hours, minutes=+minutes)).strftime(time_type)
    return now_time
