from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form--field-input', 'placeholder': 'Email Address'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = "What should we call you?"
        self.fields['email'].label = "Your good e-mail"
        self.fields['password1'].label = "Type that carefully"
        self.fields['password2'].label = "And again"



        self.fields['username'].widget.attrs['class'] = 'form--field-input'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['password1'].widget.attrs['class'] = 'form--field-input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['class'] = 'form--field-input'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form--field-input'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password'].widget.attrs['class'] = 'form--field-input'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


   