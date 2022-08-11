# Generated by Django 4.0.5 on 2022-08-11 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0028_alter_products_product_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='photo',
        ),
        migrations.AddField(
            model_name='applications',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aviato.products', verbose_name='Привязанный товар'),
            preserve_default=False,
        ),
    ]
