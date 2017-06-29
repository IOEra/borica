import datetime
import pytest
from borica import Request


class FakeSignature:
    def sign(self, content):
        return b'G' * 128


def test_general_request_base64_formatting():
    request = Request(
        transaction_type=10,
        transaction_amount='99.99',
        transaction_timestamp=datetime.datetime.fromtimestamp(0),
        terminal_id='12345678',
        order_id='12345678',
        order_summary='Money for fun!',
        signature=FakeSignature()
    )
    expected_request = (
        "MTAxOTcwMDEwMTAyMDAwMDAwMDAwMDAwOTk5OTEyMzQ1Njc4MTIzNDU2NzggICAgICAg"
        "TW9uZXkgZm9yIGZ1biEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg"
        "ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg"
        "ICAgICAgICAgICAgICAgICAgICAgICBFTjEuMEdHR0dHR0dHR0dHR0dHR0dHR0dHR0dH"
        "R0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dH"
        "R0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dH"
        "R0dH")
    assert expected_request == str(request)


def test_protocol_version_validation():
    with pytest.raises(ValueError) as excinfo:
        Request(
            transaction_type=10,
            transaction_amount='99.99',
            transaction_timestamp=datetime.datetime.fromtimestamp(0),
            terminal_id='12345678',
            order_id='12345678',
            order_summary='Money for fun!',
            signature=FakeSignature(),
            protocol_version='0.0.0'
        )
        assert 'got 0.0.0' in excinfo.value
