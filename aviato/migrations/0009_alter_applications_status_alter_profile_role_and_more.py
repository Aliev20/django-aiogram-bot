# Generated by Django 4.1.1 on 2023-04-30 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0008_alter_applications_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.CharField(blank=True, choices=[('Ожидает отправки', 'Ожидает отправки'), ('Передан логисту', 'Передан логисту'), ('Передан диспетчеру', 'Передан диспетчеру'), ('Фабричный брак', 'Фабричный брак'), ('Дорожный брак', 'Дорожный брак'), ('В дороге', 'В дороге'), ('Ожидает упаковки', 'Ожидает упаковки'), ('Упакован', 'Упакован'), ('Ожидание подтверждения', 'Ожидание подтверждения'), ('Отменен', 'Отменен'), ('Доставлен', 'Доставлен')], default='Ожидание подтверждения', max_length=200, null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Упаковщик-Логист', 'Упаковщик-Логист'), ('Снабженец', 'Снабженец'), ('Админ', 'Админ'), ('Менеджер', 'Менеджер'), ('Логист', 'Логист'), ('Оператор', 'Оператор'), ('Водитель', 'Водитель'), ('Упаковщик', 'Упаковщик')], default='', max_length=200, verbose_name='Роль пользователя'),
        ),
        migrations.AlterField(
            model_name='rolecode',
            name='role',
            field=models.CharField(choices=[('Упаковщик-Логист', 'Упаковщик-Логист'), ('Снабженец', 'Снабженец'), ('Админ', 'Админ'), ('Менеджер', 'Менеджер'), ('Логист', 'Логист'), ('Оператор', 'Оператор'), ('Водитель', 'Водитель'), ('Упаковщик', 'Упаковщик')], max_length=200, verbose_name='Роль которая выдается после активация кода'),
        ),
    ]