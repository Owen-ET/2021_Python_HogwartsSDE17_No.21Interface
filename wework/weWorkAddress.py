#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/03 11:18
# @Author  : zc
# @File    : weWorkAddress.py

from wework.base import Base


class WeWorkAddress(Base):



    def get_infomation(self,userid):
        '''读取成员'''

        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params ={
            # 'access_token': self.token,   初始化加上token了
            'userid': userid
        }
        r = self.send('GET',url,params=params,verify=False).json()
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
        # params = {
        #     'access_token': self.token
        # }


        r = self.send('POST',url,json=data,verify=False).json()
        print(r['errmsg'])



    def update_member(self,userid,name):
        '''更新成员'''
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name,
        }

        r = self.send('POST',url,json=data,verify=False).json()
        return r


    def delete_member(self,userid):
        '''删除成员'''

        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {
            # 'access_token': self.token,
            'userid': userid
        }
        r = self.send('GET',url,params=params,verify=False).json()
        return r