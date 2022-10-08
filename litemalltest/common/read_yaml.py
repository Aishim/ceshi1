import os
import yaml
import requests

def read_yaml(filename):
    file_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(file_path, filename)
    f = open( path, 'rb')
    r = f.read()
    d = yaml.safe_load(r)
    return d

