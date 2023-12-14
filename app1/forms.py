from django import forms


class TestForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
