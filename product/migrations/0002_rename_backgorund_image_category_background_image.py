# Generated by Django 5.0.3 on 2024-04-02 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='backgorund_image',
            new_name='background_image',
        ),
    ]
