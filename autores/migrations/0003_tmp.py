# Generated by Django 2.2.14 on 2020-07-14 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0002_auto_20200714_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
