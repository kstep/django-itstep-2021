from django import forms
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        exclude = []
        widgets = {
            'birthday': forms.widgets.DateInput(
                attrs={'type': 'date'}
            )
        }