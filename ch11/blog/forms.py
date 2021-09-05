# -*- coding: utf-8 -*-

# django.forms 모듈은 폼을 클래스로 표현할 수 있도록 하는 기능을 한다.
from django import forms

# 폼을 정의하기 위해서는 django.forms 모듈의 Form 클래스를 상속받아 클래스를 정의한다.
class PostSearchForm(forms.Form):
    # 폼을 정의하는 방법은 테이블의 모델 클래스를 정의하는 방법과 매우 유사하다.
    search_word = forms.CharField(label='Search Word')

