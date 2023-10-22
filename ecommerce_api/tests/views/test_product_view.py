def test_list_product_without_auth(db, client, product):
    response = client.get('/ecommerce/products/')
    assert response.status_code == 200
    assert len(response.data.get('results')) == 1

def test_retrieve_product_without_auth(db, client, product):
    response = client.get(f'/ecommerce/products/{product.id}/')
    assert response.status_code == 200
    assert response.data['id'] == product.id

def test_create_product_with_seller(db, client, user_seller, product_create_data):
    client.force_authenticate(user_seller)
    response = client.post('/ecommerce/products/', product_create_data)
    assert response.status_code == 201

def test_create_product_with_client(db, client, user_client, product_create_data):
    client.force_authenticate(user_client)
    response = client.post('/ecommerce/products/', product_create_data)
    assert response.status_code == 403

def test_update_product_with_seller(db, client, user_seller, product):
    client.force_authenticate(user_seller)
    response = client.patch(f'/ecommerce/products/{product.id}/', {"price": 200})
    assert response.status_code == 200

def test_update_product_with_client(db, client, user_client, product):
    client.force_authenticate(user_client)
    response = client.patch(f'/ecommerce/products/{product.id}/', {"price": 200})
    assert response.status_code == 403

def test_delete_product_with_seller(db, client, user_seller, product):
    client.force_authenticate(user_seller)
    response = client.delete(f'/ecommerce/products/{product.id}/')
    assert response.status_code == 204

def test_delete_product_with_client(db, client, user_client, product):
    client.force_authenticate(user_client)
    response = client.delete(f'/ecommerce/products/{product.id}/')
    assert response.status_code == 403