# Generated by Django 3.2.9 on 2021-12-02 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Collections',
            new_name='Collection',
        ),
    ]
