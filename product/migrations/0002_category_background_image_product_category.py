# Generated by Django 5.0.3 on 2024-04-03 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='category_background'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=8, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
