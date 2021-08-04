# Generated by Django 3.2.5 on 2021-08-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('br', '0041_book_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='original_title',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
