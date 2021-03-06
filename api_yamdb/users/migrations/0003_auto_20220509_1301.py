# Generated by Django 2.2.16 on 2022-05-09 13:01

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default=users.models.User.get_secret_key, max_length=64, verbose_name='Код подтверждения'),
        ),
    ]
