from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField

CATEGORY_CHOICES = (
    ('S','Shirt'),
    ('SW','Sport wear'),
    ('OW','Outwear')
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)
ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    item_category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    item_available = models.CharField(max_length=100)
    item_image = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_context = models.CharField(max_length=100)
    item_label = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateField(auto_now_add=True)
    order_date = models.DateField()
    ordered = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Payment(models.Model):
    user = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Coupon(models.Model):
    item_coupon = models.CharField(max_length=100)
    item_coupon_status = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Refund(models.Model):
    item_refund = models.CharField(max_length=100)

    def __str__(self):
        return self.title
