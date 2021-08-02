#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/02 11:44
# @Author  : zc
# @File    : test.py


import requests


class Test:

    def test_get_token(self):

        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2c06edca9d5e15ff&corpsecret=Z54tfGsdmgZfrBz09NH1WishZufGZu78D0bsq2OwsQU'
        # data = {
        #     'corpid': 'ww2c06edca9d5e15ff',
        #     'corpsecret': 'Z54tfGsdmgZfrBz09NH1WishZufGZu78D0bsq2OwsQU'
        # }

        r = requests.get(url,verify=False).json()
        print("打印:"+r['access_token'])