import pytest
from espwebsite.NetworkHandler import NetworkHandler


@pytest.fixture
def netHandler():
    return NetworkHandler()


def test_search(netHandler):
    networks = netHandler.search()
    assert type(networks) == list
