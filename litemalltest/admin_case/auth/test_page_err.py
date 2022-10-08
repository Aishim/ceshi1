import requests
import pytest
import json

def test_page401(tokk_login, host):
    '''401错误接口，当前请求需要用户验证'''
    s = tokk_login
    url_page401 = host +"admin/auth/401"
    r_page401 = s.get(url_page401)
    respond = r_page401.json()
    print(r_page401.text)
    assert respond["errno"] == 501
    assert "请登录" in respond["errmsg"]
def test_page403(tokk_login, host):
    '''403错误接口，当前请求被拒绝执行'''
    s = tokk_login
    url_page403 = host +"admin/auth/403"
    r_page403 = s.get(url_page403)
    respond = r_page403.json()
    print(r_page403.text)
    assert respond["errno"] == 506
    assert "无操作权限" in respond["errmsg"]

