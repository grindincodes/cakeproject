from __future__ import unicode_literals
from django.db import models

# Create your models here.



class Content(models.Model):
    CHOCO='CHO'
    STRAWBERRY='STR'
    VANILLA='VAN'
    REDVELVET='RED'
    FLAVOR_CHOICES=[
    (CHOCO,'초콜릿'),
    (STRAWBERRY,'딸기'),
    (VANILLA,'바닐라'),
    (REDVELVET,'레드벨벳'),
    ]
    title=models.CharField(max_length=200)
    성함=models.TextField(default='')
    연락처=models.TextField(default='')
    희망픽업일시간=models.TextField(default='')
    맛=models.CharField(
        max_length=4,
        choices=FLAVOR_CHOICES,
        default=CHOCO
    )

