from django.db import models

""" This file handles all the models I will need in this micro service
    I could obviously seperate all classes in different mini files (on class per file like in Java)
    but I consider this as a simple application and I really do not have enough time to apply all good practices.

    coded with love and enthusiasm by @eliaswalyba in Nov 22nd, 2017 
"""

class GeoPoint(models.Model):

    """ Represents a geopoint.
        A geopoint is just a simple respresentation of a real world place in the map.
        We will use this class to store the different positions used in the application.
        Since this is a REST API for a serving a mobile app which uses geolocation to retrieve locations of different spots
        to my mind this is a good way to handle that.
    """

    lat = models.FloatField()
    lon = models.FloatField()
    alt = models.FloatField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):

    """ This class represents a category of a meal in the restaurants."""

    name = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.name


class Restaurant(models.Model):

    """ This class represents a restaurant. 
        For the purpose of this project we consider that a restaurant is just a set of name and location
    """

    name = models.CharField(max_length=255)
    geopoint = models.OneToOneField(GeoPoint, on_delete=models.CASCADE)

    def _str__(self):
        return self.name


class Customer(models.Model):

    """ This class represents a customer.
        We use this class to store all people who orders a meal thru the app.
        We will just store their cellphone numbers to be able to call them back if needed.
    """

    cellphone = models.CharField(primary_key=True, max_length=15)

    def __str__(self):
        return self.cellphone


class Menu(models.Model):

    """ This class represents a menu of any restaurant. 
        A menu is a just a set of date.

        ATTENTION: I could avoid this class and just use the Meal class. 
        But I have choosen to do it like this in the purpose of extensibility and scalability
    """

    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + "=>" + self.restaurant.name


class Meal(models.Model):

    """ This class represents a meal.
        A meal is just a set of a name, a price, the menu to which it is attached and the category of the meal
    """

    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.price)


class Order(models.Model):

    """ This class represents an order.
        An order is just a set of a customer who ordered, a location to ship the order, 
        is the order validated or not and a date of the order
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    geopoint = models.ForeignKey(GeoPoint, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer.cellphone + " placed an order in " + str(self.date)


class OrderLine(models.Model):

    """ This class represents a line of an order.
        Obviously I could handle this just by adding a ManyToManyField option in the Order class
        and by repeating meals the number of times they have been ordered but this happens to be very bad for this situation
        Imagine one customer orders 5 Supu Kandia's if I don't handle it this way I will be obliged to create in the database
        5 orders for one customer which happens to be memory waste.
        This is the reason why I am using this class.
        So an order line is just a set of an order, a meal and the quantity the customer ordered of that meal
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.quantity) + " orders of " + self.meal.name