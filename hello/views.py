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
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(data=request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            age = userform.cleaned_data["age"]
            langs = userform.cleaned_data["languages"]
            dest = userform.cleaned_data["destiny"]
            return render(request, "result_test.html", {"langs_test":langs,"dest_test":dest})
            # return HttpResponse(f"""
            #     <h2>
            #     <div>Name: {name}  Age: {age}<div>
            #     <div>Languages: {langs}</div>
            #     <div>DESTINY: {dest}</div>
            #     </h2>
            # """)

        return render(request, "new_page.html", {"form": userform})

    return render(request, "new_page.html", {"form": userform})


