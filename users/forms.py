from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'container'}))
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

# class ContactForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=255)
#     email = forms.EmailField(label='Email')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#     captcha = CaptchaField()
#
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form'}))
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form'}))
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form'}))
#     password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form'}))
