# Generated by Django 4.2.5 on 2023-09-29 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_remove_deepcat_catname_category_depp_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='depp_cat',
            new_name='deep_cat',
        ),
    ]
