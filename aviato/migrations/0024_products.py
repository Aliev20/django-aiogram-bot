# Generated by Django 4.0.5 on 2022-08-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0023_remove_applications_opt_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=1000, verbose_name='Товар')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('opt_price', models.PositiveIntegerField(verbose_name='Оптовая Цена')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]