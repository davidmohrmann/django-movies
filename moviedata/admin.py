from django.contrib import admin
from .models import Rater, Movie, Rating

# Register your models here.
admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)
