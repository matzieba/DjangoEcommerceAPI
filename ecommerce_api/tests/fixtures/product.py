from model_bakery import baker
import pytest

from ecommerce_api.models import Product, ProductCategory
from ecommerce_api.serializers import ProductCategorySerializer


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