from django.urls import path

from . import views

app_name = "orm"
urlpatterns = [
    path("", views.index, name="index"),
    path("rating/", views.rating, name="rating"),
]
