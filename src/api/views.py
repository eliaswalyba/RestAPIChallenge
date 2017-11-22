from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import GeoPoint
from .models import Category
from .models import Restaurant
from .models import Customer
from .models import Menu
from .models import Meal
from .models import Order
from .models import OrderLine

from .serializers import GeoPointSerializer
from .serializers import CategorySerializer
from .serializers import RestaurantSerializer
from .serializers import CustomerSerializer
from .serializers import MenuSerializer
from .serializers import MealSerializer
from .serializers import OrderSerializer
from .serializers import OrderLineSerializer


# /api/geopoints
class GeoPointList(APIView):

    def get(self, request):
        geopoints = GeoPoint.objects.all()
        serializer = GeoPointSerializer(geopoints, many=True)
        return Response(serializer.data)
        

    def post(self):
        pass
