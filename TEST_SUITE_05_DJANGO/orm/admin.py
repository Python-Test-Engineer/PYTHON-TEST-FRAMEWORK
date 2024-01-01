from django.contrib import admin

from orm.models import Rating, Restaurant, Sale

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Sale)
admin.site.register(Rating)
