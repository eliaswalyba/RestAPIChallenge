from rest_framework import serializers
from .models import GeoPoint
from .models import Category
from .models import Restaurant
from .models import Customer
from .models import Menu
from .models import Meal
from .models import Order
from .models import OrderLine


""" This file handles all the serializers I use in this micro service
    I could obviously seperate all classes in different mini files (on class per file like in Java)
    but I consider this as a simple application and I really do not have enough time to apply all good practices.

    coded with love and enthusiasm by @eliaswalyba in Nov 22nd, 2017 
"""


class GeoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPoint
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    
class RestaurantSerializer(serializers.ModelSerializer):
    geopoint = GeoPointSerializer()
    class Meta:
        model = Restaurant
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    
class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = Menu
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    class Meta:
        model = Meal
        fields = '__all__'


class OrderLineSerializer(serializers.ModelSerializer):
    meal = MealSerializer()
    class Meta:
        model = OrderLine
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    geopoint = GeoPointSerializer()
    customer = CustomerSerializer()
    orderline = OrderLineSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
