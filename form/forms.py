from django import forms
from .models import Form

class formdata(forms.ModelForm):
    class Meta:
        model  = Form
        fields = ['name','email','date','city','phone']