from django.contrib import admin

from .models import GeoPoint
from .models import Category
from .models import Restaurant
from .models import Customer
from .models import Menu
from .models import Meal
from .models import Order
from .models import OrderLine

admin.site.register(GeoPoint)
admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderLine)
