# Generated by Django 3.2.7 on 2021-09-28 23:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0003_alter_note_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 2, 20, 40, 943827)),
        ),
    ]
