import pytest
from random import randint
import requests


@pytest.fixture(name='config')
def configuration():
    return {
        'host': 'localhost',
        'port': 5000
    }


def test_add_car(config):
    host = config['host']
    port = config['port']
    endpoint = 'add_car'

    url = 'http://{}:{}/{}'.format(host, port, endpoint)
    data = {
       "id": randint(1, 65565),
       "make": "Test",
       "model": "Test",
       "plates": "TEST {}".format(randint(0, 1000)),
       "dmv": randint(1, 65565),
       "year": randint(1900, 2017)
    }
    headers = {
        'content-type': 'application/json'
    }
    resp = requests.post(url, json=data, headers=headers)

    assert resp.status_code == 200
    assert resp.text == 'Success\n'
