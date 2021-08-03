#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/03 11:18
# @Author  : zc
# @File    : weWorkAddress.py
import requests


class WeWorkAddress:

    def __init__(self):
        self.token = self.get_token()


    def get_token(self):
        # 开代理为了抓包
        proxies = {'https': 'http://127.0.0.1:8888'}
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            'corpid': 'ww2c06edca9d5e15ff',
            'corpsecret': 'Z54tfGsdmgZfrBz09NH1WishZufGZu78D0bsq2OwsQU'
        }
        r = requests.get(url,params=params,proxies=proxies,verify=False).json()
        return r['access_token']


    def get_infomation(self,userid):
        '''读取成员'''

        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params ={
            'access_token': self.token,
            'userid': userid
        }
        r = requests.get(url,params=params,verify=False).json()
        return r


    def create_member(self,userid,name: str,mobile: str,department: list):
        '''创建成员'''
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        params = {
            'access_token': self.token
        }


        r = requests.post(url,json=data,params=params,verify=False).json()
        print(r['errmsg'])



    def update_member(self,userid,name):
        '''更新成员'''
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": userid,
            "name": name,
        }

        r = requests.post(url,json=data,verify=False).json()
        return r


    def delete_member(self,userid):
        '''删除成员'''

        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {
            'access_token': self.token,
            'userid': userid
        }
        r = requests.get(url,params=params,verify=False).json()
        return r