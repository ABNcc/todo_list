# Generated by Django 3.2.8 on 2023-05-10 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0011_alter_note_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 11, 2, 22, 15, 105639)),
        ),
    ]
