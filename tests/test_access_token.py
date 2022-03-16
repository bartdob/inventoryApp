import token
from datetime import datetime
import pytest
from inventory_api.utils import get_access_token


@pytest.mark.slow
@pytest.mark.filterwarnings
def test_create_access_token():
    print(datetime.now())
    print(get_access_token({"user_id": 1}, 1))
    print(token)
    assert isinstance(get_access_token({"user_id": 1}, 1), str)
