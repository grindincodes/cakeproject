# Generated by Django 3.2.5 on 2021-07-02 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakecollection', '0006_content_datefield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='datefield',
        ),
        migrations.AlterField(
            model_name='content',
            name='희망픽업일',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]