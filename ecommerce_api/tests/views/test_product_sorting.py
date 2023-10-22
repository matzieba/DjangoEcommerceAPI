from model_bakery import baker

def test_sort_product_by_price_ascending(db, client):
    for i in range(5):
        baker.make('ecommerce_api.Product', price=i)

    response = client.get('/ecommerce/products/?ordering=price')
    assert response.status_code == 200
    products = response.data.get('results')
    assert all(products[i]['price'] <= products[i + 1]['price'] for i in range(len(products) - 1))

def test_sort_product_by_name_ascending(db, client):
    for i in range(5):
        baker.make('ecommerce_api.Product', name=str(i))

    response = client.get('/ecommerce/products/?ordering=name')
    assert response.status_code == 200

    products = response.data.get('results')
    assert all(products[i]['name'] <= products[i + 1]['name'] for i in range(len(products) - 1))


def test_sort_product_by_category_ascending(db, client, product_category):
    for i in range(5):
        category = baker.make('ecommerce_api.ProductCategory', name=str(i))
        baker.make('ecommerce_api.Product', category=category)

    response = client.get('/ecommerce/products/?ordering=category__name')
    assert response.status_code == 200

    products = response.data.get('results')
    assert all(products[i]['category'] <= products[i + 1]['category'] for i in range(len(products) - 1))

def test_sort_product_by_price_descending(db, client):
    for i in range(5):
        baker.make('ecommerce_api.Product', price=i)

    response = client.get('/ecommerce/products/?ordering=-price')
    assert response.status_code == 200

    products = response.data.get('results')
    assert all(products[i]['price'] >= products[i + 1]['price'] for i in range(len(products) - 1))