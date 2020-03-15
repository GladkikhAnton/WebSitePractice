from django.db import models

from products.models import Product


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.PROTECT)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id  # ("Пользователь %s %s" % (self.email, seil.name)

    # Кастомизация множественного числа и единственного
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"
    def save(self, *args, **kwargs):
        price_per_item = self.product.cost
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item
        super(ProductInBasket, self).save(*args, **kwargs)
