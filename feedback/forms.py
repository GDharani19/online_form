from django import forms
from feedback.models import feedbackmodel

class feedbackform(forms.ModelForm):
    class Meta:
        model=feedbackmodel
        fields='__all__'