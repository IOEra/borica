import base64


class Response:
    def __init__(self, response):
        self._response = response

    @property
    def response_decoded(self):
        return base64.b64decode(self._response)

    def verify(self, verifier):
        payload = self.response_decoded[0:len(self.response_decoded) - 128]
        signature = self.response_decoded[56:]
        return verifier.verify(payload, signature)
