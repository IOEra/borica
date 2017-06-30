from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.Util.asn1 import DerSequence
from binascii import a2b_base64


class Verifier:
    def __init__(self, certificate):
        self._certificate = certificate

    def verify(self, payload, signature):
        key = RSA.importKey(self.public_key)
        verifier = PKCS1_v1_5.new(key)
        digest = SHA.new(payload)
        result = verifier.verify(digest, signature)
        return result is True

    @property
    def public_key(self):
        lines = self._certificate.replace(' ', '').split()
        der = a2b_base64(''.join(lines[1:-1]))

        cert = DerSequence()
        cert.decode(der)
        tbsCertificate = DerSequence()
        tbsCertificate.decode(cert[0])
        subjectPublicKeyInfo = tbsCertificate[6]

        return subjectPublicKeyInfo
