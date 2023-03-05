# Generated by Django 4.1.7 on 2023-03-01 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen_qr', '0003_alter_regist_table_regist_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='regist_table',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='regist_table',
            name='regist_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 1, 21, 59, 2, 474368), null=True, verbose_name='日時'),
        ),
    ]