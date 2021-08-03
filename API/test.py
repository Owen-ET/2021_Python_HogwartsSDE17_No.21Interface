#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/02 11:44
# @Author  : zc
# @File    : test.py
import json

import requests


class Test:

    def setup(self):
        self.token = self.get_token()


    def get_token(self):
        # 开代理为了抓包
        proxies = {'https': 'http://127.0.0.1:8888'}
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2c06edca9d5e15ff&corpsecret=Z54tfGsdmgZfrBz09NH1WishZufGZu78D0bsq2OwsQU'
        r = requests.get(url,proxies=proxies,verify=False).json()
        return r['access_token']


    def test_get_infomation(self):
        '''读取成员'''
        user_id = 'demo'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}'
        r = requests.get(url,verify=False).json()
        print(r['errmsg'])


    def create_member(self,userid,name,mobile,department):
        '''创建成员'''
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [department]
        }

        r = requests.post(url,json=data,verify=False).json()
        print(r['errmsg'])



    def test_update_member(self):
        '''更新成员'''
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": "0803csry01",
            "name": "0803更改测试人员01",
        }

        # r = requests.post(url,json=data).json()
        # print(r)



    def test_delete_member(self):
        '''删除成员'''
        userid = '0803csry03'
        name = '0803更改测试人员03'
        mobile = '13610000003'
        department = 1
        self.create_member(userid,name,mobile,department)
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}'
        r = requests.get(url,verify=False).json()
        print(r['errmsg'])
