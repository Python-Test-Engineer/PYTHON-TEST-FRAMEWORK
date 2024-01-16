"""The 4th video in the series.

"""
from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection
from django.utils import timezone
from pyboxen import boxen

from orm.models import Rating, Restaurant, Sale


def run():
    # enter code below
    print("\n===== RUNNING SCRIPT... =====\n")

    #########################################
    # View SQL queries
    count_restaurants = Restaurant.objects.count()
    c = str(connection.queries)
    output = f"Total =  {count_restaurants}"
    pprint(connection.queries)
    #########################################
