# Generated by Django 4.1 on 2022-08-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0022_alter_applications_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='bool_count',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Хватает ли количество'),
        ),
    ]