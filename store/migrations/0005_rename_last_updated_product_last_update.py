# Generated by Django 3.2.9 on 2021-11-22 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_inventory_type_product_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='last_updated',
            new_name='last_update',
        ),
    ]
