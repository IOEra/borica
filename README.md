# Borica

Low-level Python integration for Borica payment gateway.

## Usage

```
from borica import Signature, Request

key = open('path/to/private.key').read()
signature = Signature(key)

request = Request(
  transaction_type=transaction_type,
  transaction_amount=amount,
  terminal_id=62161079,
  order_id=order_id,
  order_summary=summary,
  signature=signature,
  protocol_version='1.1'
)

url = "https://gatet.borica.bg/boreps/registerTransaction?eBorica={}".format(
    str(request))
```
