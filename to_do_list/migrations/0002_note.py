# Generated by Django 3.2.7 on 2021-09-26 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('publish_date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 26, 18, 44, 52, 69793))),
            ],
        ),
    ]
