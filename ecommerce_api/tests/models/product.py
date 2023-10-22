import os
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from ecommerce_api.models import Product


def test_product_thumbnail_generation_on_create_with_seller(db, client, user_seller, product_create_data):
    file = BytesIO()
    image = Image.new('RGB', (100, 100))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)

    uploaded_image = SimpleUploadedFile(
        name='test.png',
        content=file.read(),
        content_type='image/png'
    )

    product_create_data['image'] = uploaded_image

    client.force_authenticate(user_seller)

    response = client.post('/ecommerce/products/', data=product_create_data)

    assert response.status_code == 201
    created_product_id = response.data['id']

    created_product = Product.objects.get(id=created_product_id)
    assert created_product.thumbnail is not None
    assert os.path.exists(created_product.thumbnail.path)