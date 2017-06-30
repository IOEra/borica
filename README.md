[![Build Status](https://travis-ci.org/IOEra/borica.svg?maxAge=0&branch=master)](https://travis-ci.org/IOEra/borica)
[![Coverage Status](https://coveralls.io/repos/github/IOEra/borica/badge.svg?maxAge=0&branch=master)](https://coveralls.io/github/IOEra/borica?branch=master)

# Borica

The purpose of this package is to provide low level integration with the Borica payment gateway, by implementing the basic communication protocol in Python.

## Usage

### Preparing BOReq

```
from borica import Signature, Request

key = open('BOReq_Test.key').read()
signature = Signature(key)

request = Request(
  transaction_type=10,
  transaction_amount='0.09',
  terminal_id=62168888,
  order_id='422242',
  order_summary='Order summary',
  signature=signature,
  protocol_version='1.1'
)

eBorica = str(request)
```

### Handling BOResp

```
verifier = Verifier(open('certificate.pem').read())
response = Response(eBorica)
assert response.verify(verifier) is True
assert response.status_code == 0
```
