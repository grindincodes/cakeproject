# Generated by Django 3.2.5 on 2021-07-02 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakecollection', '0007_auto_20210703_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='희망픽업일',
            field=models.CharField(default=datetime.date.today, max_length=30, null=True),
        ),
    ]
