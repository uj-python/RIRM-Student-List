from django import forms
from django.db.models import fields
from .models import StudentAcademics
from .models import Studentsinfo


class student_info_form(forms.ModelForm):

    class Meta:
        model=Studentsinfo
        fields="__all__"
        


class student_academics_form(forms.ModelForm):

    class Meta:
        model=StudentAcademics
        fields=('Maths','Physics','Chemistry','Biology','English')



