import pytest
from user_admin.models import CustomUser, UserActivities, CustomUserManager


@pytest.mark.slow
@pytest.mark.filterwarnings
@pytest.mark.django_db
def test_custom_user_create():
    CustomUser.objects.create_superuser('test@test.pl', 'test')
    assert CustomUser.objects.count() == 1


@pytest.mark.skip
def test_superuser_create():
    CustomUserManager.create_superuser('test@test.pl', 'test', 'test')
    assert CustomUserManager.objects.count() == 1
