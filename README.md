# DjangoEcommerceAPI
A Django 4 and Django REST Framework based eCommerce API that provides various functionalities including product listing, order management, product management, and user role-based authentication. Features pagination, filtering, sorting, email notifications, and automated thumbnail generation.


Local usage:
1. create env
2. run pip install -r requirements.txt
3. run python manage.py runserver 0.0.0.0:8000
4. run python manage.py migrate


Tests suite usage:
1. run pytest


Creating DockerImage:
1. docker build -t your_image_name .