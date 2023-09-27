from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render

from .forms import UserForm
from .models import Person

def index(request):
    userform = UserForm()
    return render(request, "new_page.html", {"form": userform})


def postuser(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(data=request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            age = userform.cleaned_data["age"]
            langs = userform.cleaned_data["languages"]
            dest = userform.cleaned_data["destiny"]
            slide = userform.cleaned_data["slider"]
            # СОхраненеи в базу
            name_bd = Person.objects.create(name=name, age=age, languages=langs, destiny=dest, slider=slide)




            data = {"langs_test": langs, "dest_test": dest, "slide": slide, "NAME": name, "AGE": age}
            return render(request, "result_test.html", context=data)


        return render(request, "new_page.html", {"form": userform})

    return render(request, "new_page.html", {"form": userform})


