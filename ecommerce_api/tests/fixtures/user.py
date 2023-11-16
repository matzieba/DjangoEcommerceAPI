from model_bakery import baker
import pytest
from ecommerce_api.models import User


@pytest.fixture()
def user_client():
    return baker.make(
        User,
        email='email@email.com',
    )


@pytest.fixture()
def user_seller():
    user = baker.make(
        User,
    )
    user.is_staff = True
    user.save()
    return user
