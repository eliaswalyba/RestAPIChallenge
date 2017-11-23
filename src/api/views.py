from django.shortcuts import get_object_or_404
from django.http import Http404
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


""" This file handles all the views I use to render the ressources.
    I could obviously seperate all classes in different mini files (on class per file like in Java)
    but I consider this as a simple application and I really do not have enough time to apply all good practices.

    coded with love and enthusiasm by @eliaswalyba in Nov 22nd, 2017 
"""


class GeoPointList(APIView):

    def get(self, request):
        geopoints = GeoPoint.objects.all()
        serializer = GeoPointSerializer(geopoints, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = GeoPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeoPointDetail(APIView):

    def get_object(self, pk):
        try:
            return GeoPoint.objects.get(pk=pk)
        except GeoPoint.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = GeoPointSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        geopoint = self.get_object(pk)
        serializer = GeoPointSerializer(geopoint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):

    def get_object(self, name):
        try:
            return Category.objects.get(pk=name)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        serializer = CategorySerializer(self.get_object(name))
        return Response(serializer.data)

    def put(self, request, name, format=None):
        category = self.get_object(name)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        self.get_object(name).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestaurantList(APIView):

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):

    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = RestaurantSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerList(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):

    def get_object(self, cellphone):
        try:
            return Customer.objects.get(pk=cellphone)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, cellphone, format=None):
        serializer = CustomerSerializer(self.get_object(cellphone))
        return Response(serializer.data)

    def put(self, request, cellphone, format=None):
        customer = self.get_object(cellphone)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cellphone, format=None):
        self.get_object(cellphone).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MenuList(APIView):

    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetail(APIView):

    def get_object(self, pk):
        try:
            return Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = MenuSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MealList(APIView):

    def get(self, request):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealDetail(APIView):

    def get_object(self, pk):
        try:
            return Meal.objects.get(pk=pk)
        except Meal.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = MealSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        meal = self.get_object(pk)
        serializer = MealSerializer(meal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = OrderSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderLineList(APIView):

    def get(self, request):
        orderlines = OrderLine.objects.all()
        serializer = OrderLineSerializer(orderlines, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = OrderLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderLineDetail(APIView):

    def get_object(self, pk):
        try:
            return OrderLine.objects.get(pk=pk)
        except OrderLine.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = OrderLineSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        orderline = self.get_object(pk)
        serializer = OrderLineSerializer(orderline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)