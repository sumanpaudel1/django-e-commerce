# Generated by Django 4.2.7 on 2024-05-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
