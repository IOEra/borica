import base64
import binascii


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
        return int(self.payload[51:53].decode())
