from django.contrib import admin
from .models import Stock, StockName

# Register your models here.
admin.site.register(Stock)
admin.site.register(StockName)
