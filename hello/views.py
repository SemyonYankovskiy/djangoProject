from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render


def index(request):
    data = {"n": 5}
    return render(request, "new_page.html", context=data)
