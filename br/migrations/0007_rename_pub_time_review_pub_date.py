# Generated by Django 3.2.5 on 2021-07-21 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('br', '0006_review_pub_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='pub_time',
            new_name='pub_date',
        ),
    ]
