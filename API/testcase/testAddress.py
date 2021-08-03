#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/03 11:42
# @Author  : zc
# @File    : testAddress.py
import pytest

from API.wework.weWorkAddress import WeWorkAddress


class TestAddress:

    name1 = '0803更改测试人员03'

    def setup_class(self):
        self.address = WeWorkAddress()
        self.userid = '0803csry03'
        self.name = '0803测试人员03'
        # self.name1 = '0803更改测试人员03'
        self.mobile = '13610000003'
        self.department = [1]
        print("===========class_start===========")


    def teardown_class(self):
        print("===========class_stop===========")


    def setup(self):
        print("===========case_start===========")
        self.address.delete_member(self.userid)


    def teardown(self):
        print("===========case_close===========")
        # self.address.delete_member(self.userid)


    def test_get_infomation(self):

        self.address.create_member(self.userid,self.name,self.mobile,self.department)

        po = self.address.get_infomation(self.userid)
        print(po)
        assert po.get('name') == self.name,"与返回结果不匹配"

    @pytest.mark.parametrize("new_name",[name1+'_No1',name1+'_No2',name1+'_No3',name1+'_No4'])
    def test_update_member(self,new_name):
        print(new_name)
        self.address.create_member(self.userid, self.name, self.mobile, self.department)
        po = self.address.update_member(self.userid,new_name)
        assert po['errmsg'] == 'updated'

        info = self.address.get_infomation(self.userid)
        assert info['name'] == new_name



    def test_delete_member(self):
        self.address.create_member(self.userid, self.name, self.mobile, self.department)
        po = self.address.delete_member(self.userid)
        assert po['errmsg'] == 'deleted'

        info = self.address.get_infomation(self.userid)
        assert info['errcode'] == 60111