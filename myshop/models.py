from django.db import models
import datetime
from django.utils import timezone

class Customer(models.Model):
    id = models.AutoField(primary_key=True,)
    full_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.full_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    quantity = models.PositiveIntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    quantity = models.IntegerField()
    date_added = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class ShippingAddress(models.Model):
    order_date = models.DateTimeField()
    contact = models.CharField(max_length=14, blank=True, null=True)
    shipping_address = models.CharField(max_length=100, blank=True, null=True)
    shipping_city = models.CharField(max_length=50, blank=True, null=True)
    shipping_state = models.CharField(max_length=50, blank=True, null=True)
    shipping_country = models.CharField(max_length=50, blank=True, null=True)
    shipping_zip_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'myshop_shipping_address'


class Order(models.Model):
    quantity = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=5)
    status = models.CharField(max_length=20)
    order_date = models.DateTimeField(blank=True, null=True)
    orderitem = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
    shipping = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=5)
    payment_date = models.DateTimeField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

