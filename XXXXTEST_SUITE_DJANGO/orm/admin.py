from django.contrib import admin
from orm.models import Restaurant, Sale, Rating

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Sale)
admin.site.register(Rating)
