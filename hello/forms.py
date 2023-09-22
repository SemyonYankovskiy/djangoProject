from django import forms


class UserForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20)
    age = forms.IntegerField(min_value=1, max_value=100)
    languages = forms.ChoiceField(choices=[
        ("Python", "python"),
        ("JavaScript", "js"),
        ("C++", "c++"),
        ("Java", "java")
    ])
