from django import forms
from django.core.validators import RegexValidator


class UserForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, validators=[RegexValidator(r"^[а-яА-Я]+$")])
    age = forms.IntegerField(min_value=1, max_value=100)
    languages = forms.ChoiceField(choices=[
        ("Python", "python"),
        ("JavaScript", "js"),
        ("C++", "c++"),
        ("Java", "java")
    ])
    destiny = forms.ChoiceField(choices=[
        ("RAVE","rave"),
        ("VODKA", "vodka"),
        ("IT", "it"),
    ])
