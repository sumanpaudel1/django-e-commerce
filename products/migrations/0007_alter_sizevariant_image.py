# Generated by Django 4.2.7 on 2024-04-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_sizevariant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizevariant',
            name='image',
            field=models.ImageField(default=True, upload_to='product'),
        ),
    ]