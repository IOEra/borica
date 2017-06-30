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
            payload = self.response_decoded[0:len(self.response_decoded) - 128]
            signature = self.response_decoded[56:]
            return verifier.verify(payload, signature)
        except binascii.Error:
            return False
