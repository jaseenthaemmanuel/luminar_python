from django import forms
from base.models import LoginModel

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = ["usrnm", "pwd"]

class RegisterForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = "__all__"