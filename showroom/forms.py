
from django import forms
from .models import Bike
#this is ModelForm. used to create form directly from
#django model. it for building forms tied to database object
class Bikeform(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['name', 'company', 'price']

#when we want full  control and not tied to Model.
#means not in model we use here.
# from django import forms
# class Bikeform(forms.Form):
#     name = forms.CharField(max_length=100)
#     message = forms.CharField(max_length=100)
#     price = forms.IntegerField()
#     email = forms.EmailField()
#     password = forms.PasswordInput()