# Generated by Django 4.2.6 on 2023-10-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userinfo_username_alter_userinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]
