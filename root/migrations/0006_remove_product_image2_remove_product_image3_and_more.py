# Generated by Django 4.2.5 on 2023-10-03 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0005_product_image2_product_image3_product_image4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image5',
        ),
    ]