from django import forms
from django.core.validators import RegexValidator


class UserForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, validators=[RegexValidator(r"^[а-яА-Яa-zA-Z]+$")], label="Имя")
    age = forms.IntegerField(min_value=1, max_value=100, label="Возраст")
    languages = forms.ChoiceField(choices=[
        ("", "Выберите значение"),
        ("python", "Python"),
        ("js", "JavaScript"),
        ("c++", "C++"),
        ("java", "Java")
    ], label="Язык программирования")
    destiny = forms.ChoiceField(choices=[
        ("", "Выберите значение"),
        ("rave","RAVE"),
        ("vodka", "VODKA"),
        ("it", "IT"),
    ], label="Сфера работы")
    slider = forms.IntegerField(

        # min_value=1,
        # max_value=100,
        label="Номер телефона",
        widget=forms.TextInput(attrs={"type": "range", "min": 79780000000, "max": 79789999999, "class": "form-range", "id": "slider"})
    )
