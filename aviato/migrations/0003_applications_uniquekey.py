# Generated by Django 4.2 on 2023-04-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0002_alter_applications_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='uniqueKey',
            field=models.CharField(default=1, max_length=5000, verbose_name='Уникальный идентификатор'),
            preserve_default=False,
        ),
    ]