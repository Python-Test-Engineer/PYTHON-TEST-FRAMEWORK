from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from orm.models import Restaurant, Rating, Sale


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "restaurant_type")


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ("rating", "restaurant")
        # widgets = {
        #     "rating": forms.NumberInput(
        #         attrs={
        #             "min": 1,
        #             "max": 5,
        #             "step": 1,
        #         }
        #     )
        # }
        # validators = [
        #     MinValueValidator(1),
        #     MaxValueValidator(5),
        # ]
