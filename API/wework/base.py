#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/04 10:43
# @Author  : zc
# @File    : base.py
import requests


class Base:

    def __init__(self):
        # 加上sesson提高运行效率
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {'access_token': self.token}



    def get_token(self):


        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            'corpid': 'ww2c06edca9d5e15ff',
            'corpsecret': 'Z54tfGsdmgZfrBz09NH1WishZufGZu78D0bsq2OwsQU'
        }
        r = self.s.get(url, params=params, verify=False).json()

        # 开代理为了抓包
        # proxies = {'https': 'http://127.0.0.1:8888'}
        # r = requests.get(url,params=params,proxies=proxies,verify=False).json()

        return r['access_token']



    def send(self,*args, **kwargs):
        return self.s.request(*args, **kwargs)

