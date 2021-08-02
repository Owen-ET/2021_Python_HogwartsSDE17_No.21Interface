#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/02 11:44
# @Author  : zc
# @File    : test.py


import requests


class Test:

    def setup(self):
        self.token = self.get_token()


    def get_token(self):

        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2c06edca9d5e15ff&corpsecret=Z54tfGsdmgZfrBz09NH1WishZufGZu78D0bsq2OwsQU'
        r = requests.get(url,verify=False).json()
        return r['access_token']


    def test_get_infomation(self):

        user_id = 'demo'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}'
        r = requests.get(url,verify=False).json()
        print(r)