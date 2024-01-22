"""The 8th video in the series. Many-to-many relationships."""
from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection
from django.utils import timezone
from pyboxen import boxen
from colorama import Fore, Back, Style
from orm.models import Rating, Restaurant, Sale, StaffRestaurant, Staff
from django.db.models.functions import Lower


def run():
    # enter code below
    print(f"\n{Fore.GREEN }  ===== RUNNING SCRIPT... =====")
    # print(Style.RESET_ALL)

    staff, created = Staff.objects.get_or_create(name="Sally Carter")
    restaurant = Restaurant.objects.first()
    restaurant2 = Restaurant.objects.last()
    # staff2 = Staff.objects.get(pk=2)
    staff = Staff.objects.get(pk=3)
    StaffRestaurant.objects.create(staff=staff, restaurant=restaurant2, salary=18_000)
    print(Fore.BLUE + str(staff))
    print(Fore.BLUE + str(created))
    print("\n")
    print(Fore.YELLOW + str(connection.queries))
    print("\n")
