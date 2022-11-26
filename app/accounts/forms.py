from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', required=True)
    password = forms.CharField(label='Password', required=True)
    next = forms.CharField(required=False, widget=forms.HiddenInput)


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm password', strip=False, required=True,
                                       widget=forms.PasswordInput)
    username = forms.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Incorrect password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
