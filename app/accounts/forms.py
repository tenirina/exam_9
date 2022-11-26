from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', required=True)
    password = forms.CharField(label='Password', required=True)
    next = forms.CharField(required=False, widget=forms.HiddenInput)
