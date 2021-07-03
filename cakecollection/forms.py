#from typing import ContextManager
from django import forms
#from django.forms import fields
from .models import Content
class ContentForm(forms.ModelForm):
    class Meta:
        model=Content
        fields=['가게이름','성함','연락처','희망픽업일','희망픽업시간','맛','모양','사이즈','원하시는도안사진첨부',]