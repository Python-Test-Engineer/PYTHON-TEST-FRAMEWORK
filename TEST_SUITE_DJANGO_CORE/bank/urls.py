from django.urls import path

from . import views

urlpatterns = [
    path("", views.bank_homepage, name="homepage"),
]
