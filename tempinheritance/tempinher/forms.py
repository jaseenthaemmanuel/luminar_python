from django import forms
from tempinher.models import Employee

class Loginform(forms.ModelForm):
    class Meta:
        model = Employee
        #exclude = ["field1", "field2"]
        #include = {"field1", "field2"}
        fields = ["username", "password"]


class Registerf(forms.ModelForm):
    confirm_pwd = forms.CharField(max_length=100)
    class Meta:
        model = Employee
        fields = ["name", "age", "salary", "desig", "phonenum","username", "password", "confirm_pwd"]
