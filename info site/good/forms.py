# from django import forms

from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileField, ClearableFileInput


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }


# class UserForm(forms.Form):
#     Email = forms.EmailField(label="Логин", help_text="Введите свой Email_@")
#     password = forms.CharField(label="Пароль", help_text="Введите свой Пароль")
#     comment = forms.CharField(label="Комментарий", widget=forms.Textarea)

    # field_order = ["age", "name", "comment"]

    # # url = forms.URLField(label="metanit", type="https://metanit.com/python/django/4.2.php")
    # comment = forms.CharField(label="Комментарий", widget=forms.Textarea)
