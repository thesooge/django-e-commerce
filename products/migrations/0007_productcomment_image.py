# Generated by Django 4.2.15 on 2024-08-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_productcomment_slug_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcomment',
            name='image',
            field=models.ImageField(blank=True, upload_to='products_covers/'),
        ),
    ]
