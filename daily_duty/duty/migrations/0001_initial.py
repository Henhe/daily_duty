# Generated by Django 3.1.5 on 2021-02-24 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator("^['А-Я']['а-я']+")], verbose_name='Haзвaниe месяца')),
                ('name_int', models.PositiveSmallIntegerField(db_index=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(13)], verbose_name='Порядковый номер месяца в году')),
            ],
            options={
                'verbose_name': 'Месяц',
                'verbose_name_plural': 'Месяцы',
                'ordering': ['name_int'],
            },
        ),
    ]
