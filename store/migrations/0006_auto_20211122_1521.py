# Generated by Django 3.2.9 on 2021-11-22 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_last_updated_product_last_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment_at',
            new_name='placed_at',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='unite_price',
            new_name='unit_price',
        ),
    ]
