from django import forms
from books.models import Bookmodel

class Bookform(forms.ModelForm):
    class Meta():
        model = Bookmodel
        fields = '__all__'



