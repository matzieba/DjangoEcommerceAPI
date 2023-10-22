from model_bakery import baker
import pytest

from ecommerce_api.models import Product, ProductCategory


@pytest.fixture()
def product():
    return baker.make(
        Product
    )

@pytest.fixture()
def product_category():
    return baker.make(ProductCategory)

@pytest.fixture()
def product_create_data(product_category):
    return {
        "name": "Product",
        "category": product_category.pk,
        "price": 100
    }