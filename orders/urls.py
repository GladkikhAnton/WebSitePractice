from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from orders import views

urlpatterns = [
    path('basket/', views.basket, name="basket"),
    path('basket_adding/', views.basket_adding, name='basket_adding'),
    path('changing_nmb_basket/', views.changing_nmb_basket, name="changing_nmb_basket"),
    path('deleting_product/', views.deleting_product, name='deleting_product'),
]
