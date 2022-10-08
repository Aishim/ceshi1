import requests
import pytest
import json


def test_logout_1(tokk_login, host):
    '''退出登录接口'''
    s = tokk_login
    url_logout= host +"admin/auth/logout"
    r_logout = s.post(url_logout)
    respond = r_logout.json()
    print(r_logout.text)
    assert respond["errno"] == 0
    assert "成功" in respond["errmsg"]

def test_logout_2( host ):
    '''没有给头部 传登录token'''
    s = requests.session()
    logout_url = host + "admin/auth/logout"
    r_logout = s.post(logout_url)
    respond = r_logout.json()
    assert r_logout.status_code == 200
    assert respond["errno"] == 501
    assert "请登录" in respond["errmsg"]