import token
from datetime import datetime
import pytest
from inventory_api.utils import get_access_token, decodeJWT


@pytest.mark.slow
@pytest.mark.filterwarnings
def test_create_access_token():
    print(datetime.now())
    print(get_access_token({"user_id": 1}, 1))
    print(token)
    assert isinstance(get_access_token({"user_id": 1}, 1), str)


@pytest.mark.slow
@pytest.mark.filterwarnings
def test_decode_token():
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9' \
            '.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ' \
            '.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c '
    print(type(decodeJWT(token)))
    assert isinstance(decodeJWT(token), object)
