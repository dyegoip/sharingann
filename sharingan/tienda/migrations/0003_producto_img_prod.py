# Generated by Django 5.0.6 on 2024-07-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_tipo_prod'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img_prod',
            field=models.ImageField(null=True, upload_to='tienda'),
        ),
    ]
