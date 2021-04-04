from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=50)
    #phone_number = PhoneField(blank=True, help_text='Contact phone number')
    phone_number=models.CharField(max_length=50)
    def __str__(self):
        return str(self.user)

CATEGORY_CHOICES=(
    ('M','MOBILE'),
    ('L','Laptop'),
    ('T','Tshirt'),
)


class Product(models.Model):
    title=models.CharField(max_length=200)
    sellingprice=models.FloatField()
    discountprice=models.FloatField()
    discription=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2,default='M')
    brand=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to="productimage")
    
    def __str__(self):
        return str(self.title)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.user)

