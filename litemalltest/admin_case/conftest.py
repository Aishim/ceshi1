import requests
import pytest
from litemalltest.admin_case.login import login
from litemalltest.common.execute_mysql import *

@ pytest.fixture(scope="function")
def tokk_login():
    s = requests.Session()
    login(s)
    return s

@ pytest.fixture(scope="function")
def del_data():
    sql = "delete from litemall_role where name='test1'"
    execu_sql(sql)
