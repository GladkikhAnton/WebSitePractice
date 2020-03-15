from django.contrib import admin

from orders.models import ProductInBasket


class ProductInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]
    class Meta:
        model = ProductInBasket
admin.site.register(ProductInBasket, ProductInBasketAdmin)
