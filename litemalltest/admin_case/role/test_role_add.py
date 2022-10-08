import pytest
import requests
import re
import json

def test_role_add_1(tokk_login, host, del_data):
    '''必填项正常填写，新增角色成功'''
    s = tokk_login
    url_radd = host + "admin/role/create"
    body = {
        "addTime": "",
        "deleted": False,
        "desc": "测试1",
        "enabled": True,
        "id": 3,
        "name": "test1",
        "updateTime": ""    #  2022-10-04 22:39:50 2022-10-04T12:27:42.790Z
    }
    r_add = s.post(url_radd, json=body)
    respond = r_add.json()
    assert respond["errno"] == 0

    print(r_add.text)