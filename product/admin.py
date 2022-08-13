from django.contrib import admin
from .models import Foods, Categories, Pricing

# Register your models here.

admin.site.register(Foods)
admin.site.register(Categories)
admin.site.register(Pricing)