from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def validate_restaurant_name_begins_with_a(value):
    if not value.startswith("a"):
        raise ValidationError('Restaurant name must begin with "a"')


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = "IN", "Indian"
        CHINESE = "CH", "Chinese"
        ITALIAN = "IT", "Italian"
        GREEK = "GR", "Greek"
        MEXICAN = "MX", "Mexican"
        FASTFOOD = "FF", "Fast Food"
        OTHER = "OT", "Other"

    # swap this out for below to restict to only the choices begining with a
    # name = models.CharField(
    #     max_length=100, validators=[validate_restaurant_name_begins_with_a]
    # )
    name = models.CharField(max_length=100)
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField(
        default=0.0, validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        default=0.0, validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(f"print out state from def save in model: {self._state.adding}")
        super().save(*args, **kwargs)


class Rating(models.Model):
    # one restaurant can have many ratings but a rating can only have one restaurant
    user = models.PositiveIntegerField(default=1)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="ratings"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"Rating: {self.rating}"


class Sale(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.SET_NULL, null=True, related_name="sales"
    )
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()


class Staff(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ManyToManyField(Restaurant, through="StaffRestaurant")

    class Meta:
        verbose_name_plural = "Staff"

    def __str__(self):
        return self.name


class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField(default=10_000.00, null=True)

    class Meta:
        verbose_name_plural = "Staff Restaurant"

    def __str__(self):
        return f"{self.staff} - {self.restaurant} - {self.salary}"
