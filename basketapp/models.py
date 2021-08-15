from django.db import models
from django.conf import settings
from mainapp.models import Product
from django.utils.functional import cached_property


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super().save(*args, **kwargs)

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = self.get_items_cached
        _totalquantity = sum([x.quantity for x in _items])
        return _totalquantity

    @property
    def total_cost(self):
        _items = self.get_items_cached
        _totalcost = sum(x.product_cost for x in _items)
        return _totalcost

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user)

    # def delete(self):
    #     print('Удален')
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super(self.__class__, self).delete()

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(id=pk)
