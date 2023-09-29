# Generated by Django 4.2.5 on 2023-09-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='future',
            name='img',
            field=models.ImageField(default='images/default/default.png', upload_to='image/future'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(default='image/default/default.png', upload_to='image/portfolio'),
        ),
    ]
