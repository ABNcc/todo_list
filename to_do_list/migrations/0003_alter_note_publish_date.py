# Generated by Django 3.2.8 on 2022-05-31 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0002_alter_note_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 31, 10, 37, 18, 992708)),
        ),
    ]
