from django import forms
from .models import Mytopic

class mytopicform(forms.ModelForm):
    class Meta:
        model = Mytopic
        fields = ['topic', 'description']