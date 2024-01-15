"""The second video in the series.
Django-extensions runscript: https://django-extensions.readthedocs...
Django filter(): https://docs.djangoproject.com/en/4.2...
Django - Following Relations Backward: https://docs.djangoproject.com/en/4.2...
"""
from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection
from django.utils import timezone
from pyboxen import boxen

from orm.models import Rating, Restaurant, Sale

# python manage.py shell_plus --print-sql can be used to view sql from console
#
# Restaurant.objects.first() gives...
# SELECT "orm_restaurant"."id",
#        "orm_restaurant"."name",
#        "orm_restaurant"."website",
#        "orm_restaurant"."date_opened",
#        "orm_restaurant"."latitude",
#        "orm_restaurant"."longitude",
#        "orm_restaurant"."restaurant_type"
#   FROM "orm_restaurant"
#  ORDER BY "orm_restaurant"."id" ASC
#  LIMIT 1
# Execution time: 0.001000s [Database: default]
# <Restaurant: Pizzeria 1>


def run():
    # enter code below
    print("\n===== RUNNING SCRIPT... =====\n")

    #########################################
    # View SQL queries
    # count_restaurants = Restaurant.objects.count()
    # c = str(connection.queries)
    # output = f"Total =  {count_restaurants}"
    # pprint(connection.queries)
    #########################################

    # print(
    #     boxen(
    #         output,
    #         padding=1,
    #         margin=1,
    #         color="blue",
    #     )
    # )

    # print(
    #     boxen(
    #         c,
    #         padding=1,
    #         margin=1,
    #         color="green",
    #     )
    # )

    # # Rich renderables, with a mix of strings and renderables
    # from rich.table import Table
    #
    # table = Table(show_header=True, header_style="bold magenta")
    # table.add_column("Date", style="dim", width=12)
    # table.add_column("Title")
    # table.add_column("Production Budget", justify="right")
    # table.add_column("Box Office", justify="right")
    # table.add_row(
    #     "Dec 20, 2019",
    #     "Star Wars: The Rise of Skywalker",
    #     "$275,000,000",
    #     "$375,126,118",
    # )
    #
    # table.add_row(
    #     "May 25, 2018",
    #     "[red]Solo[/red]: A Star Wars Story",
    #     "$275,000,000",
    #     "$393,151,347",
    # )
    #
    # table.add_row(
    #     "Dec 15, 2017",
    #     "Star Wars Ep. VIII: The Last Jedi",
    #     "$262,000,000",
    #     "[bold]$1,332,539,889[/bold]",
    # )
    #
    # print(boxen("Python is cool!", table))
    # chinese = Restaurant.TypeChoices.CHINESE
    # indian = Restaurant.TypeChoices.INDIAN
    # mexican = Restaurant.TypeChoices.MEXICAN
    # check_types = [chinese, indian, mexican]

    # restaurants = Restaurant.objects.filter(restaurant_type__in=check_types)
    # print(restaurants)
    # pprint(connection.queries)

    # Restaurant.objects.create(
    #     name="TEST",
    #     date_opened=timezone.now(),
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN,
    # )
    # print(Restaurant.objects.last())
    # print(Restaurant.objects.first())

    # restaurant = Restaurant.objects.last()
    # user = 3
    # Rating.objects.create(user=user, restaurant=restaurant, rating=4)
    # print(Rating.objects.first())
    # pprint(connection.queries)

    # print("1: ", Rating.objects.filter(restaurant__name__startswith="T").count())
    # print("2: ",Rating.objects.filter(restaurant__date_opened__year=2023).count())
    # print("3: ",Rating.objects.filter(restaurant__date_opened__month=11).count())
    # print("4: ",Rating.objects.filter(rating__gte=3).count())
    # print("5: ", Rating.objects.exclude(rating__gte=3).count())
    # print("6: ", Rating.objects.exclude(rating__gte=3))
    # pprint(connection.queries)

    # restaurant = Restaurant.objects.first()
    # print(restaurant.name)
    # restaurant.name = "2 UPDATED AGAIN"
    # restaurant.save()
    # print(restaurant.name)
    # pprint(connection.queries)

    # JOIN QUERY
    # rating to parent model Reastaurant
    # rating = Rating.objects.first()
    # print(rating.rating)
    # print(rating.restaurant.date_opened)
    # print(rating.restaurant)
    # print(rating.restaurant.name)
    # Parent Restaurant to child model Rating
    # restaurant = Restaurant.objects.first()
    # has this related_name set in model othewise use rating_set
    # print(restaurant.ratings.all())
    # related_name set in model
    # print(restaurant.sales.all())
    # pprint(connection.queries)

    # restaurant = Restaurant.objects.last()
    # print(Rating.objects.get_or_create(user=2, restaurant=restaurant, rating=1))
    # # output is (<Rating: Rating: 1>, True) with True meaning it was created and not updated.
