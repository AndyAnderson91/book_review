# Generated by Django 3.2.5 on 2021-07-21 12:16

import br.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('br', '0002_auto_20210721_1139'),
    ]
    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
