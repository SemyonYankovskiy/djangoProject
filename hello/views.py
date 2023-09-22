from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    userform = UserForm()
    return render(request, "new_page.html", {"form": userform})


def postuser(request):
    if request.method == "POST":
        userform = UserForm(data=request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            age = userform.cleaned_data["age"]
            langs = userform.cleaned_data["languages"]
            return HttpResponse(f"""
                <h2>
                <div>Name: {name}  Age: {age}<div>
                <div>Languages: {langs}</div>
                </h2>
            """)

        return render(request, "new_page.html", {"form": userform})

    return render(request, "index.html")


