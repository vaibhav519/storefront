# Generated by Django 3.2.9 on 2021-12-02 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_collections_collection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='collections',
            new_name='collection',
        ),
    ]
