from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from orm.models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "restaurant_type")
