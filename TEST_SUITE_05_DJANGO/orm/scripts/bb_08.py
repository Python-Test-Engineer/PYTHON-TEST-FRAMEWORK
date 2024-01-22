"""The 8th video in the series. Many-to-many relationships."""
from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection
from django.utils import timezone
from pyboxen import boxen
from colorama import Fore, Back, Style
from orm.models import Rating, Restaurant, Sale, StaffRestaurant, Staff
from django.db.models.functions import Lower
import random


def run():
    # enter code below
    print(f"\n{Fore.GREEN }  ===== RUNNING SCRIPT... =====")
    # print(Style.RESET_ALL)

    staff, created = Staff.objects.get_or_create(name="Sally Carter")
    # restaurant = Restaurant.objects.first()
    # restaurant2 = Restaurant.objects.last()
    # # staff2 = Staff.objects.get(pk=2)
    # staff = Staff.objects.get(pk=3)
    # StaffRestaurant.objects.create(staff=staff, restaurant=restaurant2, salary=18_000)

    # staff_restaurants = StaffRestaurant.objects.filter(staff=staff)
    # print(staff_restaurants)
    # for s in staff_restaurants:
    #     print(s.salary)
    # print(Fore.BLUE + str(staff))
    # print(Fore.BLUE + str(created))

    # r1 = Restaurant.objects.first()
    # r2 = Restaurant.objects.last()
    # staff.restaurant.add(r1, through_defaults={"salary": 50_000})
    # staff.restaurant.add(r2, through_defaults={"salary": 10_000})

    # staff.restaurant.set(
    #     Restaurant.objects.all()[:10],
    #     through_defaults={"salary": lambda: random.randint(10_000, 50_000)},
    # )
    s = StaffRestaurant.objects.prefetch_related("staff", "restaurant")
    print(s)
    print("\n")
    print(Fore.YELLOW + str(connection.queries))
    print("\n")
