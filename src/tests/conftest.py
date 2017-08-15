import pytest
import src


@pytest.fixture
def app():
    return src.app
