# Generated by Django 3.2.5 on 2021-07-21 12:16

import br.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('br', '0002_auto_20210721_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='born',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), br.models.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('first_name', 'patronymic', 'last_name', 'born')},
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'year')},
        ),
    ]
