from django.core.validators import RegexValidator
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20, validators=[RegexValidator(r"^[а-яА-Яa-zA-Z]+$")])
    age = models.IntegerField()
    languages = models.CharField(max_length=20)
    destiny = models.CharField(max_length=20)
    slider = models.IntegerField()
