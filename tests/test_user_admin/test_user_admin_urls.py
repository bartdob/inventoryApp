from rest_framework.test import APIClient
import pytest


@pytest.mark.slow
@pytest.mark.skip("skip for now")
def test_users_url():
    client = APIClient()
    response = client.get(path='/user/users', format='json')
    assert response.status_code == 200