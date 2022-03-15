import pytest
from user_admin.models import CustomUser


@pytest.mark.filterwarnings
@pytest.mark.django_db
def test_user_create():
    CustomUser.objects.create_superuser('test@test.pl', 'test')
    assert CustomUser.objects.count() == 1
