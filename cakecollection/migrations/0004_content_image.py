# Generated by Django 3.2.5 on 2021-07-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakecollection', '0003_auto_20210702_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
