import base64
import binascii
from datetime import datetime


class Response:
    def __init__(self, response):
        self._response = response

    @property
    def response_decoded(self):
        return base64.b64decode(self._response)

    def verify(self, verifier):
        try:
            signature = self.response_decoded[56:]
            return verifier.verify(self.payload, signature)
        except (binascii.Error, TypeError):
            return False

    @property
    def payload(self):
        return self.response_decoded[0:len(self.response_decoded) - 128]

    @property
    def status_code(self):
        return int(self._get_field(51, 53))

    @property
    def transaction_code(self):
        return int(self._get_field(0, 2))

    @property
    def transaction_time(self):
        return datetime.strptime(self._get_field(2, 16), '%Y%m%d%H%M%S')

    @property
    def amount(self):
        return int(self._get_field(16, 28)) / 100.0

    @property
    def terminal_id(self):
        return int(self._get_field(28, 36))

    @property
    def order_id(self):
        return self._get_field(31, 51)

    @property
    def protocol_version(self):
        return self._get_field(53, 56)

    def _get_field(self, start, end):
        return self.payload[start:end].decode()
