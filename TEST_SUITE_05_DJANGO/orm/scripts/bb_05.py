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
    #  count_restaurants = Restaurant.objects.count()
    #  c = str(connection.queries)
    #  output = f"Total =  {count_restaurants}"
    #  print("Count: ", output)
    #  pprint(connection.queries)
    #########################################

    # restaurant = Restaurant.objects.first()
    # # print(restaurant.name)
    # restaurant.name = "New Restaurant"
    # restaurant.save() # saves all fields and with def save overwritten in models.py it will print true or false if new or updated
    # print(restaurant.name)
    # pprint(connection.queries)
    # restaurant.save(update_fields=["name"])

    # def save will return True
    # restaurant = Restaurant()
    # restaurant.name = "My Italian Restaurant"
    # restaurant.date_opened = timezone.now()
    # restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    # restaurant.latitude = 50.2
    # restaurant.longitude = 50.5
    # restaurant.save()
    # pprint(connection.queries)

    # restaurants = Restaurant.objects.all()
    # restaurants.update(date_opened=timezone.now())

    # restaurants = Restaurant.objects.filter(name__startswith="M")
    # print(restaurants)
    # print(
    #     "Total Updated =",
    #     restaurants.update(
    #         date_opened=timezone.now() - timezone.timedelta(days=365),
    #         website="https://www.test.com",
    #     ),
    # )
    # # just one query is run

    #  cascade delete
    # restaurant = Restaurant.objects.first()
    # print(restaurant.pk)
    # print(restaurant.ratings.all())
    # restaurant.delete()

    # cascade Null on Sale model - will leave Null in resaurant_id
    restaurants = Restaurant.objects.filter(id=77)
    restaurants.delete()

    pprint(connection.queries)
