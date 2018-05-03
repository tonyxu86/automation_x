#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Administrator
@file: WinRemote.py
@time: 2018/5/3 0003 下午 10:17
"""
import winrm


class WinRemote(object):

    def __init__(self):
        pass

    def runcommond(self):
        s = winrm.Session('192.168.1.3:5985/wsman', auth=('Administrator', '1234'))
        r = s.run_cmd('dir')
        return r

if __name__ == '__main__':
    pass

t = WinRemote()
result = t.runcommond()

