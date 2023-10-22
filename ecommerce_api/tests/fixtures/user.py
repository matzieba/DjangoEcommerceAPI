from model_bakery import baker
import pytest
from ecommerce_api.models import User

@pytest.fixture()
def user_client():
    return baker.make(
        User,
        type='client',
        email='email@email.com',
    )

@pytest.fixture()
def user_seller():
    return baker.make(
        User,
        type='seller'
    )