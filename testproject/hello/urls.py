from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("mongolian/", views.bymongolian, name="bymongolian"),
    # path("chinese/", views.bychinese, name="bychinese"),
    # path("<str:language>", views.greetings, name="greetings"),
    path("<str:language>", views.greetings, name="greetings"),
]
