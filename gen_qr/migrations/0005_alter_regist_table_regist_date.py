# Generated by Django 4.1.7 on 2023-03-01 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen_qr', '0004_regist_table_image_alter_regist_table_regist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regist_table',
            name='regist_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 1, 22, 9, 40, 754188), null=True, verbose_name='日時'),
        ),
    ]
