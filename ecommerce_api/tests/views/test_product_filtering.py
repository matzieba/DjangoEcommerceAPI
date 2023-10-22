from decimal import Decimal


def test_list_product_filter_by_name(db, client, product):
    response = client.get(f'/ecommerce/products/?name={product.name}')
    assert response.status_code == 200
    result_product = next(iter(response.data.get('results')), None)
    assert result_product['name'] == product.name

def test_list_product_filter_by_description(db, client, product):
    response = client.get(f'/ecommerce/products/?description={product.description}')
    assert response.status_code == 200
    result_product = next(iter(response.data.get('results')), None)
    assert result_product['description'] == product.description

def test_list_product_filter_by_category(db, client, product):
    response = client.get(f'/ecommerce/products/?category__name={product.category.name}')
    assert response.status_code == 200
    result_product = next(iter(response.data.get('results')), None)
    assert result_product['category'] == product.category.id

def test_list_product_filter_by_price(db, client, product):
    response = client.get(f'/ecommerce/products/?price={product.price}')
    assert response.status_code == 200
    result_product = next(iter(response.data.get('results')), None)
    assert Decimal(result_product['price']) == product.price