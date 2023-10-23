import os
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files import File
from PIL import Image
from django.db import models
from django.db.models.fields.files import ImageFieldFile

THUMBNAIL_SIZE = (200, 200)

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    class Meta:
        ordering = ['id']

    def save(self, *args, **kwargs):
        making_thumbnail = False

        if self.image and not self.thumbnail:
            making_thumbnail = True

        super().save(*args, **kwargs)

        if making_thumbnail:
            self.thumbnail = self.generate_thumbnail(self.image)
            self.save()

    def generate_thumbnail(self, image: ImageFieldFile) -> File:
        image_obj = Image.open(image).convert('RGB')
        image_obj.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        thumb_name, thumb_extension = os.path.splitext(image.name)
        thumb_extension = thumb_extension.lstrip('.')
        thumb_filename = thumb_name + '_thumb.' + thumb_extension

        temp_thumb = BytesIO()
        image_obj.save(temp_thumb, thumb_extension)
        temp_thumb.seek(0)

        return ContentFile(temp_thumb.read(), name=thumb_filename)