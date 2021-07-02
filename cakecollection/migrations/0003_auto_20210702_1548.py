# Generated by Django 3.2.5 on 2021-07-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakecollection', '0002_auto_20210702_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='모양',
            field=models.CharField(choices=[('원형', '원형'), ('하트', '하트'), ('사각형', '사각형')], default='원형', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='사이즈',
            field=models.CharField(choices=[('도시락케이크(1~2인)', '도시락케이크(1~2인)'), ('1호(2~3인)', '1호(2~3인)'), ('2호(3~4인)', '2호(3~4인)'), ('3호(4~5인)', '2호(4~5인)')], default='도시락케이크', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='맛',
            field=models.CharField(choices=[('초콜릿', '초콜릿'), ('딸기', '딸기'), ('바닐라', '바닐라'), ('레드벨벳', '레드벨벳')], default='초콜릿', max_length=4, null=True),
        ),
    ]