# Generated by Django 3.2.8 on 2021-12-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='url',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
