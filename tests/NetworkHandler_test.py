import pytest
from espwebsite.NetworkHandler import NetworkHandler

ssid = "50:02:91:FD:EB:59_network"
password = "espdefault"
client = {
    "mac": "50:02:91:FD:EB:59"
}


@pytest.fixture
def netHandler():
    return NetworkHandler()


def test_search(netHandler):
    networks = netHandler.search()
    print(networks)
    assert type(networks) == set or networks == False


def test_connect(netHandler):
    assert netHandler.connect(ssid, password) == True


def test_disconnect(netHandler):
    netHandler.disconnect()


def test_connectClient(netHandler):
    status = netHandler.connectClient(client)
    print(status)
    assert type(status) == bool
