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
    # print(Style.RESET_ALL)

    print("\n")
    print(Fore.YELLOW + str(connection.queries))
    print("\n")
