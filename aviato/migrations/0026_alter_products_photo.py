# Generated by Django 4.0.5 on 2022-08-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0025_products_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Фото'),
        ),
    ]
