import pytest
from espwebsite.NetworkHandler import NetworkHandler


@pytest.fixture
def netHandler():
    return NetworkHandler()


def test_search(netHandler):
    networks = netHandler.search()
    print(networks)
    assert type(networks) == set


def test_connect(netHandler):
    ssid = "50:02:91:FD:EB:59_network"
    password = "espdefault"
    assert netHandler.connect(ssid, password) == True


def test_disconnect(netHandler):
    netHandler.disconnect()
