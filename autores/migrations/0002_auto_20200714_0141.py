# Generated by Django 2.2.14 on 2020-07-14 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
