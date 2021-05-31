import pytest
from espwebsite.NetworkHandler import NetworkHandler

ssid = "50:02:91:FD:EB:59_network"
password = "espdefault"
client = {
    "mac": "50:02:91:FD:EB:59",
    "ip": "192.168.178.49"
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
    assert status == True


def test_disconnectClient(netHandler):
    status = netHandler.disconnectClient(client)
    assert status == True


def test_getConnected(netHandler):
    devices = netHandler.getConnected()
    assert type(devices) == list
