from __future__ import unicode_literals
try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus
from base64 import b64encode
import datetime


class Request:
    TRANSACTION_TYPES = [
        10,  # Authorization
        11,  # Payment
        21,  # Request delayed authorization
        22,  # Execute delayed authorization
        23,  # Reverse request delayed authorization
        40,  # Reversal
        41,  # Reverse payment
    ]

    PROTOCOL_VERSIONS = [
      '1.0',
      '1.1',
      '2.0'
    ]

    CURRENCIES = [
      'USD',
      'EUR',
      'BGN'
    ]

    def __init__(
            self,
            transaction_type,
            transaction_amount,
            terminal_id,
            order_id,
            order_summary,
            signature,
            one_time_ticket='',
            transaction_timestamp=None,
            language='EN',
            protocol_version='1.0',
            currency='EUR'):
        if transaction_timestamp is None:
            transaction_timestamp = datetime.datetime.now()

        self.transaction_type = self.validate(
            int(transaction_type), of=self.TRANSACTION_TYPES)
        self.transaction_timestamp = transaction_timestamp
        self.transaction_amount = str(transaction_amount).replace('.', '')
        self.terminal_id = terminal_id
        self.order_id = order_id
        self.order_summary = order_summary
        self.language = str(language).upper()
        self.protocol_version = self.validate(
            str(protocol_version), of=self.PROTOCOL_VERSIONS)
        self.currency = self.validate(
            str(currency).upper(), of=self.CURRENCIES)
        self.one_time_ticket = one_time_ticket
        self.signature = signature

    def __str__(self):
        signed_content = self.signature.sign(self.unsigned_content)
        payload = self.unsigned_content.encode('utf-8') + signed_content
        return quote_plus(b64encode(payload).decode('utf-8'))

    @staticmethod
    def validate(value, of):
        try:
            assert value in of
            return value
        except AssertionError:
            raise ValueError('Expected on of {0} got {1}'.format(
                str(of), str(value)))

    @staticmethod
    def fill(object, length, char=' ', right=False):
        truncated = str(object)[0:length]
        just = [truncated.ljust, truncated.rjust][right]
        return just(length, str(char))

    @property
    def unsigned_content(self):
        return ''.join([
            self.fill(self.transaction_type, 2),
            self.fill(self.transaction_timestamp.strftime('%Y%m%d%H%M%S'), 14),
            self.fill(self.transaction_amount, 12, char='0', right=True),
            self.fill(self.terminal_id, 8),
            self.fill(self.order_id, 15),
            self.fill(self.order_summary, 125),
            self.fill(self.language, 2),
            self.fill(self.protocol_version, 3),
            (self.fill(self.currency, 3)
                if self.protocol_version > '1.0' else ''),
            self.one_time_ticket if self.protocol_version == '2.0' else ''
        ])
