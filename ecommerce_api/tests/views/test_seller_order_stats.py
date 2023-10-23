from freezegun import freeze_time


@freeze_time("2023-10-28 07:19:33")
def test_order_stats(db, client, user_seller, orders, product1, product2, order_stats_data):
    client.force_authenticate(user=user_seller)

    response = client.get("/ecommerce/order-stats/", data=order_stats_data)

    assert response.status_code == 200

    stats_data = response.json()

    assert len(stats_data) == 2

    first_product_stat = stats_data[0]
    second_product_stat = stats_data[1]

    assert first_product_stat["product"] == product1.pk
    assert first_product_stat["orders"] == 5

    assert second_product_stat["product"] == product2.pk
    assert second_product_stat["orders"] == 3


@freeze_time("2023-10-28 07:19:33")
def test_order_stats_result_limit(db, client, user_seller, orders, product1, product2, order_stats_data_1):
    client.force_authenticate(user=user_seller)

    response = client.get("/ecommerce/order-stats/", data=order_stats_data_1)

    assert response.status_code == 200

    stats_data = response.json()

    assert len(stats_data) == 1

    first_product_stat = stats_data[0]

    assert first_product_stat["product"] == product1.pk
    assert first_product_stat["orders"] == 5
