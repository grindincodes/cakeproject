# Generated by Django 3.2.5 on 2021-07-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakecollection', '0008_alter_content_희망픽업일'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='title',
        ),
        migrations.AddField(
            model_name='content',
            name='가게이름',
            field=models.CharField(default='OO cake', max_length=200),
        ),
    ]
