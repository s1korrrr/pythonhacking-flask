import time

import pytest
from flask import url_for


def test_add_car(client):
    resp = client.get(url_for('some_json'))
    assert resp.status_code == 200
    assert len(resp.json) == 2

    epoch = int(resp.json['epoch_time'])
    assert time.time() == pytest.approx(epoch, abs=1)
