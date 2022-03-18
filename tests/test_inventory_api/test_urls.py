from rest_framework.test import APIClient
import pytest


@pytest.mark.slow
def test_user_url():
    client = APIClient()
    response = client.get(path='/user/', format='json')
    assert response.status_code == 200


@pytest.mark.slow
def test_admin_url():
    client = APIClient()
    response = client.get(path='/admin/', format='json')
    assert response.status_code == 302

