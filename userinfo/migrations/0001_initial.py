# Generated by Django 2.0.6 on 2018-07-02 06:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
