from datetime import datetime, timedelta
from django.conf import settings
import pytest
from inventory_api.utils import get_access_token


@pytest.mark.skip
@pytest.mark.filterwarnings
def test_create_access_token():
    print(get_access_token(("user_id", 1), 1))
    # assert get_access_token(payload, 1) == 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOiIxMjM0NTY3ODkwIn0' \
    #                                        '.zcdoVgPcafWmLd67EaAkMTFyD0iD74jz5FCC7WCbL_Q '