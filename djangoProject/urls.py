

from django.urls import path
from hello import views

urlpatterns = [

    path("", views.index),
    path("postuser", views.postuser),
    path("check", views.get_from_base),
    path("delete_info", views.delete_from_base),

]