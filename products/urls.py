from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product')
]
