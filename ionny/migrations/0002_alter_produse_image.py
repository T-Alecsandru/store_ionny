# Generated by Django 4.0.2 on 2022-02-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ionny', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produse',
            name='image',
            field=models.ImageField(default='static/not_image.jpg', upload_to='static/product_images/'),
        ),
    ]
