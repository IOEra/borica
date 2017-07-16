# -*- coding: utf-8 -*-
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
        transaction_timestamp=datetime.datetime(1970, 1, 1, 2, 0),
        terminal_id='12345678',
        order_id='12345678',
        order_summary=u'Money for fun!'.encode('cp1251'),
        signature=FakeSignature()
    )
    print(str(request))
    expected_request = (
        "MTAxOTcwMDEwMTAyMDAwMDAwMDAwMDAwOTk5OTEyMzQ1Njc4MTIzNDU2NzggICAgICAg"
    )
    assert str(request).startswith(expected_request)


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
