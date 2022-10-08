import requests
import pytest
import json


def test_info(tokk_login,host):
    '''用户信息接口'''
    s = tokk_login
    url_info= host +"admin/auth/info"

    r_info = s.get(url_info)
    respond = r_info.json()
    print(r_info.text)
    assert respond["errno"] == 0
    assert "成功" in respond["errmsg"]
    assert bool(respond["data"]["roles"]) != 0