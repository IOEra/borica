import Crypto.PublicKey.RSA as RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA


class Signature:
    def __init__(self, key):
        self._key = key

    def sign(self, content):
        rsakey = RSA.importKey(self._key)
        signer = PKCS1_v1_5.new(rsakey)
        digest = SHA.new(content.encode('utf-8'))
        return signer.sign(digest)
