# Generated by Django 2.0.6 on 2018-07-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20180709_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, upload_to='item/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, upload_to='review/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='photo',
            field=models.ImageField(blank=True, upload_to='shop/%Y/%m/%d'),
        ),
    ]
