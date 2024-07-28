from src.oklink_py.protocol import ProtocolType
from src.oklink_py.config import Config
from src.oklink_py.oklink import Oklink
import pytest
import requests


# Mocking requests.get to avoid actual API calls during testing
class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

def mock_requests_get(*args, **kwargs):
    return MockResponse()

@pytest.fixture
def oklink():
    return Oklink(Config.api_key)

def test_address_info(monkeypatch, oklink):
    monkeypatch.setattr(requests, "get", mock_requests_get)
    result = oklink.address_info(Config.test1)
    assert result == {"mock_key": "mock_response"}

def test_address_active_chain(monkeypatch, oklink):
    monkeypatch.setattr(requests, "get", mock_requests_get)
    result = oklink.address_active_chain(Config.test1)
    assert result == {"mock_key": "mock_response"}

def test_address_token_balance(monkeypatch, oklink):
    monkeypatch.setattr(requests, "get", mock_requests_get)
    result = oklink.address_token_balance(Config.test1, ProtocolType.token_20)
    assert result == {"mock_key": "mock_response"}

# TODO: Add more tests for other methods in oklink.py