from model_bakery import baker
import pytest

from ecommerce_api.models import Product, ProductCategory



@pytest.fixture()
def product(product_category):
    product = baker.make(
        Product,
        description='Product no 1'
    )
    product.category = product_category
    product.save()
    return product

@pytest.fixture()
def product_category():
    return baker.make(
        ProductCategory,
        name='category'
    )

@pytest.fixture()
def product_create_data(product_category):
    return {
        "name": "Product",
        "category": product_category.id,
        "price": 100
    }

@pytest.fixture()
def product1(product_category):
    product = baker.make(
        Product,
        description='Product no 1',
        price=50,
    )
    return product

@pytest.fixture()
def product2(product_category):
    product = baker.make(
        Product,
        description='Product no 2',
        price=100,
    )
    return product