from borica import Signature


DUMMY_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDTb6056fGwtczLFM2I2qeCCatBdPgF2Gt0qH0toD8LaMEV52Kx
v8PyUXa1zZul90/nWCvcJgX/tSCYG8+u2eoVVp82bVrIbVfI8DB1qTJIwO3fROBs
ZDa5SwHs4sgQJlXB5QW1OuP0Zow9zUiYuMDcBakZLhkRGWmqYTEoHbelfQIDAQAB
AoGBALP0ceg/wBBZu3MBQqn/B+C6oAK3Lj2zZEnG+buyjtYEE4q0BCErCPgd875q
v9Xy9xP8zF+0ERkBLTupOAsmt35i9pw2TYYzmhLPrnuwKJeexe/qcz6BlI8BdJY4
LVIe59AUnKjH624HaxluIRlqNclcLpiSiJOi6AhUMeSxJ1UBAkEA+HndLgQ7cZ+S
u9ZRwKoyNIy7PFXDSMHDu7XaIbUqD9Pi/W3sEq95RlSwVRsyhzF/8efCZLiLkSI1
C8UYK9H0PQJBANnWsAuS6PiK15xQI1FjNk5p25OV7GsTcB5o+/kJRMAxLpv45OE7
O39FOJEEoeSWf5Yqz/fgqSr8BggcO3n7SkECQDfTCUJBaSmJ9GmHKS7kDguIYriX
fBxojBUsMinIjf6oWCMgAx3flpuag1NbnOqK0HgE3cPLQnAFA231hgyySvECQBd3
fTeB9/7uVhPMvkFCQtNnq/PWLsXKLkXYYWyOhw19Ptwmj+GDlAE9374flaEeZVgz
/HtjhFXRGIU/JVkarQECQQC+ebP9KFaQ5Q312H38LZfIiGHgQh75aYjeH8J1i/Ac
LCuCOXtm+vayM4WXYwyrPdjGhD6RNW5rot2QRNS0xIIz
-----END RSA PRIVATE KEY-----"""


def test_signature():
    signature = Signature(DUMMY_KEY)
    bytes_result = signature.sign('Something very secret')
    result = 0
    for b in bytes_result:
        try:
            result = result + ord(b)
        except TypeError:
            result = result + int(b)
    assert result == 16511
