import pytest
import requests
import re
import json

host = "http://127.0.0.1:9527/"
#s = requests.Session()
def login(s):

    login_url = host + "admin/auth/login"
    login_body = {
        "code": "",
        "username": "admin123",
        "password": "admin123"
    }
    r_login = s.post(login_url, json=login_body)
    respond = r_login.json()

    #cok = re.findall("Cookie:(.+?)", r_login.headers())
    cok = r_login.cookies
    s.cookies.update(cok)

    tok = respond["data"]["token"]
    c = requests.cookies.RequestsCookieJar()
    c.set("X-Litemall-Admin-Token", tok)
    s.cookies.update(c)

    return tok