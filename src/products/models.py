from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    # strip_product_id = ''

    name = models.CharField(max_length=120)
    handle = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=9.99)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, default=9.99)

    strip_price = models.IntegerField(default=0)
    price_changed_timestamp = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.price != self.original_price:
            # price changed
            self.original_price = self.price
            # trigger an api request for the price
            self.strip_price = int(self.price * 100)
            self.price_changed_timestamp = timezone.now()
        super().save(*args, **kwargs)
