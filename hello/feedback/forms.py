from django.forms import Form
from django import forms


class FeedbackForm(Form):
    sender = forms.EmailField(required=True)
    subject = forms.CharField(required=False)
    message = forms.CharField(required=True,
                              widget=forms.Textarea)