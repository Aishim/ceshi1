import os
import pytest
@ pytest.fixture(scope="function")
def host():
    os.environ["_host"] = "http://127.0.0.1:9527/"
    host = os.environ["_host"]
    return host