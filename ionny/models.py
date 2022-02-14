from django.db import models


# Create your models here.

class Produse(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/product_images/', default='static/not_image.jpg')
    promoted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.price}'


class Contact(models.Model):
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    anunt = models.TextField(null=True)

    def __str__(self):
        return f'{self.phone} - {self.email}'
