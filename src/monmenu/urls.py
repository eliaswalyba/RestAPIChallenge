from django.conf.urls import url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/geopoints/$', views.GeoPointList.as_view()),
    url(r'^api/geopoints/(?P<pk>[0-9]+)/$', views.GeoPointDetail.as_view()),

    url(r'^api/categories/$', views.CategoryList.as_view()),
    url(r'^api/categories/(?P<name>[\s\S]+)/$', views.CategoryDetail.as_view()),

    url(r'^api/restaurants/$', views.RestaurantList.as_view()),
    url(r'^api/restaurants/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view()),

    url(r'^api/customers/$', views.CustomerList.as_view()),
    url(r'^api/customers/(?P<cellphone>[0-9]{9})/$', views.CustomerDetail.as_view()),

    url(r'^api/menus/$', views.MenuList.as_view()),
    url(r'^api/menus/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view()),

    url(r'^api/meals/$', views.MealList.as_view()),
    url(r'^api/meals/(?P<pk>[0-9]+)/$', views.MealDetail.as_view()),

    url(r'^api/orders/$', views.OrderList.as_view()),
    url(r'^api/orders/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),

    url(r'^api/orderlines/$', views.OrderLineList.as_view()),
    url(r'^api/orderlines/(?P<pk>[0-9]+)/$', views.OrderLineDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)