# Generated by Django 5.0.6 on 2024-07-12 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_store_custo_last_na_e6a359_idx_store_custo_last_na_2e448d_idx_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
