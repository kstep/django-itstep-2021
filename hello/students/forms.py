from django import forms
from django.forms import widgets
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        exclude = []
        widgets = {
            'birthday': widgets.DateInput(
                attrs={'type': 'date'}
            )
        }