from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection
from django.utils import timezone
from pyboxen import boxen

from orm.models import Rating, Restaurant, Sale


def run():
    # enter code below
    print("\n===== RUNNING SCRIPT... =====\n")
    count_restaurants = Restaurant.objects.count()
    c = str(connection.queries)
    output = f"Total =  {count_restaurants}"
    # pprint(connection.queries)
    print(
        boxen(
            output,
            padding=1,
            margin=1,
            color="blue",
        )
    )

    print(
        boxen(
            c,
            padding=1,
            margin=1,
            color="green",
        )
    )

    # Rich renderables, with a mix of strings and renderables

    from rich.table import Table

    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Date", style="dim", width=12)
    table.add_column("Title")
    table.add_column("Production Budget", justify="right")
    table.add_column("Box Office", justify="right")
    table.add_row(
        "Dec 20, 2019",
        "Star Wars: The Rise of Skywalker",
        "$275,000,000",
        "$375,126,118",
    )
    table.add_row(
        "May 25, 2018",
        "[red]Solo[/red]: A Star Wars Story",
        "$275,000,000",
        "$393,151,347",
    )
    table.add_row(
        "Dec 15, 2017",
        "Star Wars Ep. VIII: The Last Jedi",
        "$262,000,000",
        "[bold]$1,332,539,889[/bold]",
    )

    print(boxen("Python is cool!", table))

    chinese = Restaurant.TypeChoices.CHINESE
    indian = Restaurant.TypeChoices.INDIAN
    mexican = Restaurant.TypeChoices.MEXICAN
    check_types = [chinese, indian, mexican]

    restaurants = Restaurant.objects.filter(restaurant_type__in=check_types)
    print(restaurants)
    pprint(connection.queries)
