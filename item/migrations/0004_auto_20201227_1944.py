# Generated by Django 3.1.4 on 2020-12-27 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_package_trade'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostCategory',
            new_name='ProductCategory',
        ),
    ]
