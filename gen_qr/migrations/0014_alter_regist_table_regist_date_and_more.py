# Generated by Django 4.1.7 on 2023-03-04 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen_qr', '0013_alter_regist_table_regist_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regist_table',
            name='regist_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 4, 21, 13, 23, 189188), null=True, verbose_name='日時'),
        ),
        migrations.AlterField(
            model_name='temp_image',
            name='regist_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 4, 21, 13, 23, 188186), null=True, verbose_name='日時'),
        ),
    ]
