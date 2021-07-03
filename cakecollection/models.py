from __future__ import unicode_literals
from django.db import models
import datetime
# Create your models here.



class Content(models.Model):
    TIME_CHOICES=[
        ('10:00','10:00'),
        ('10:30','10:30'),
        ('11:00','11:00'),
        ('11:30','11:30'),
        ('12:00','12:00'),
        ('12:30','12:30'),
        ('13:00','13:00'),
        ('14:30','14:30'),
        ('15:00','15:00'),
        ('15:30','15:30'),
        ('16:00','16:00'),
        ('16:30','16:30'),
        ('17:00','17:00'),
        ('17:30','17:30'),
        ('18:00','18:00'),
        ('18:30','18:30'),
        
    ]
    FLAVOR_CHOICES=[
    ('초콜릿','초콜릿'),
    ('딸기','딸기'),
    ('바닐라','바닐라'),
    ('레드벨벳','레드벨벳'),
    ]
    SHAPE_CHOICES=[
        ('원형','원형'),
        ('하트','하트'),
        ('사각형','사각형'),
    ]
    SIZE_CHOICES=[
        ('도시락케이크(1~2인)','도시락케이크(1~2인)'),
        ('1호(2~3인)','1호(2~3인)'),
        ('2호(3~4인)','2호(3~4인)'),
        ('3호(4~5인)','2호(4~5인)'),
    ]

    가게이름=models.CharField(max_length=200, default="OO cake")
    성함=models.CharField(max_length=200)
    연락처=models.CharField(max_length=200)
    희망픽업일= models.CharField(null=True,max_length=30,default=datetime.date.today)
    희망픽업시간=models.CharField(
        null=True,
        max_length=30,
        choices=TIME_CHOICES,
        default='10:00')
    맛=models.CharField(
        null=True,
        max_length=4,
        choices=FLAVOR_CHOICES,
        default='초콜릿')
    모양=models.CharField(
        null=True,
        max_length=5,
        choices=SHAPE_CHOICES,
        default="원형"
    )
    사이즈=models.CharField(
        null=True,
        max_length=30,
        choices=SIZE_CHOICES,
        default="도시락케이크"
    )
    원하시는도안사진첨부 = models.ImageField(null=True,upload_to='images/', blank=True)
    

