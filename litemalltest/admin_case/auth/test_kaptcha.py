import requests
import pytest
import json


def test_kaptcha(tokk_login, host):
    '''验证码接口'''
    s = tokk_login
    url_kaptcha= host +"admin/auth/kaptcha"
    r_kaptcha = s.get(url_kaptcha)
    respond = r_kaptcha.json()
    print(r_kaptcha.text)
    assert respond["errno"] == 0
    assert "成功" in respond["errmsg"]
    assert bool(respond["data"]) != 0

