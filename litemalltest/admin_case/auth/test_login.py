import pytest
import requests
import re
import json
from litemalltest.common.read_yaml import read_yaml

def test_login_1(tokk_login, host):
    '''admin123登录，账号密码正确'''
    s = tokk_login
    login_url = host + "admin/auth/login"
    login_body = {
        "code": 1,
        "username": "admin123",
        "password": "admin123"
    }
    r_login = s.post(login_url, json=login_body)
    respond = r_login.json()
    # tok = respond["data"]["token"]
    assert "成功" in respond["errmsg"]
    assert respond["errno"] == 0

def test_login_2(tokk_login, host):
    '''账号不存在，密码正确'''
    s = tokk_login
    login_url = host + "admin/auth/login"
    login_body = {
        "code": "",
        "username": "admin",
        "password": "admin123"
    }
    r_login = s.post(login_url, json=login_body)
    respond = r_login.json()
    assert respond["errno"] == 605


def test_login_3(tokk_login, host):
    '''账号存在，密码不正确'''
    s = tokk_login
    login_url = host + "admin/auth/login"
    login_body = {
        "code": "",
        "username": "admin123",
        "password": "admin"
    }
    r_login = s.post(login_url, json=login_body)
    respond = r_login.json()
    assert respond["errno"] == 605


filename = "login_data.yaml"
data = read_yaml(filename)
@ pytest.mark.parametrize("username", data["username"])
@ pytest.mark.parametrize("password", data["password"])
def test_login_4(tokk_login, host, username, password):
    '''账号不存在，密码不正确'''
    s = tokk_login
    login_url = host + "admin/auth/login"
    login_body = {
        "username": username,
        "password": password
    }
    r_login = s.post(login_url, json=login_body)
    respond = r_login.json()
    assert respond["errno"] == 605


def test_login_5(tokk_login, host):
    '''多传一个参数'''
    s = tokk_login
    login_url = host + "admin/auth/login"
    login_body = {
        "code": "",
        "username": "admin123",
        "password": "admin123",
        "paramd": "多的参数"
    }
    r_login = s.post(login_url, json=login_body)
    print(r_login.text)
    assert r_login.status_code ==200
    assert bool(r_login.json()["data"]) == 0
    assert bool(r_login.json()["errmsg"]) == 0
    assert bool(r_login.json()["errno"]) == 0


def test_login_6(tokk_login, host):
    '''少传一个参数 password'''
    s = tokk_login
    login_url = host + "admin/auth/login"
    login_body = {
        "username": "admin123",
    }
    r_login = s.post(login_url, json=login_body)
    print(r_login.text)
    assert r_login.json()["errmsg"] == "参数不对"
    assert r_login.json()["errno"] == 401

