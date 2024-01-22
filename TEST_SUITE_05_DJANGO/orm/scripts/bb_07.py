"""The 6th video in the series."""
from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection
from django.utils import timezone
from pyboxen import boxen
from colorama import Fore, Back, Style
from orm.models import Rating, Restaurant, Sale
from django.db.models.functions import Lower


def run():
    # enter code below
    print(f"\n{Fore.GREEN }  ===== RUNNING SCRIPT... =====")
    # print(Fore.RED + "some red text")
    # print(Back.GREEN + "and with a green background")
    # print(Style.DIM + "and in dim text")
    # print(Style.RESET_ALL)
    # print("back to normal now")
    print(Style.RESET_ALL)

    # restuarants = Restaurant.objects.filter(
    #     restaurant_type=Restaurant.TypeChoices.CHINESE
    # )
    # restaurants = Restaurant.objects.filter(name="Mexican 1")
    # print(restaurants)
    # print(restaurants.count())
    # print(restaurants.get()) # get() for 1 item only
    # restaurants = Restaurant.objects.get(name="Mexican 1")

    # restaurants = Restaurant.objects.filter(
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN
    # )
    # print(restaurants.exists())
    # for r in restaurants:
    #     print(r.name)

    # restaurants = Restaurant.objects.filter(
    #     restaurant_type=chinese, name__startswith="C"  # AND
    # )
    # for r in restaurants:
    #     print(f"{Fore.BLUE + r.name}")

    chinese = Restaurant.TypeChoices.CHINESE
    indian = Restaurant.TypeChoices.INDIAN
    mexican = Restaurant.TypeChoices.MEXICAN

    # check_types = [chinese, indian, mexican]
    # restaurants = Restaurant.objects.filter(restaurant_type__in=check_types)
    # for r in restaurants:
    #     print(f"{Fore.BLUE + r.name}")

    # restaurants = Restaurant.objects.exclude(restaurant_type=chinese)
    # restaurants = Restaurant.objects.exclude(restaurant_type__in=[chinese, indian])
    # restaurants = Restaurant.objects.filter(name__lt="E")  # A to D
    # restaurants = Restaurant.objects.filter(longitude__gt=10)
    # for r in restaurants:
    #     print(f"{Fore.BLUE + r.name}")

    # sales = Sale.objects.filter(income__gt=90)
    # sales = Sale.objects.filter(income__range=(50, 60))
    # sales = Sale.objects.filter(income__range=(50, 60)).order_by("income")
    # for sale in sales:
    #     print(f"{Fore.GREEN + str(sale.income)}")

    # restaurants = Restaurant.objects.filter(longitude__lt=-1.0).order_by("-name")
    # for r in restaurants:
    #     print(f"{Fore.BLUE + r.name + str(r.longitude)}")

    #  r = Restaurant.objects.first()
    #  r.name = r.name.lower()
    #  r.save()
    # restaurants = Restaurant.objects.order_by("name")  # lower case last
    # restaurants = Restaurant.objects.order_by(
    #     Lower("name")
    # )  # lower case in right place case insensitive
    #  restaurants = Restaurant.objects.order_by("-date_opened")[0:3]

    # for r in restaurants:
    #     print(f"{Fore.BLUE  + r.name  + ' - ' + r.date_opened.strftime('%d %b %Y') }")
    # once can set default ordering in model via:
    # Class Meta:
    #   ordering = [Lower("-name")] - import Lower from django.db.models.functions import Lower

    # r = Restaurant.objects.earliest("date_opened")
    # print(f"{Fore.BLUE  + r.name  + ' - ' + r.date_opened.strftime('%d %b %Y') }")

    # ratings = Rating.objects.filter(restaurant__name__startswith="C")
    # print(ratings)

    # sales = Sale.objects.filter(restaurant__restaurant_type=chinese)
    # print(sales)

    print("\n")
    print(Fore.YELLOW + str(connection.queries))
    print("\n")
