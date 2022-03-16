import pytest
from user_admin.models import CustomUser, UserActivities


@pytest.mark.skip("test is ok, for now will skiped")
@pytest.mark.filterwarnings
@pytest.mark.django_db
def test_custom_user_create():
    CustomUser.objects.create_superuser('test@test.pl', 'test')
    assert CustomUser.objects.count() == 1


@pytest.mark.skip
def test_user_activities():
    pass
