# Generated by Django 2.0.6 on 2018-07-11 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0006_userinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='photo',
        ),
    ]
