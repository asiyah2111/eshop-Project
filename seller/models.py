from django.db import models
from Eshop.models import UserProfile

# Create your models here.
class Category(models.Model):
	catname = models.CharField(max_length=50)

class Product(models.Model):
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=200)
	price = models.DecimalField(decimal_places=2, max_digits=12)
	qty = models.IntegerField()
	pro_img = models.ImageField(upload_to="product_image", blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	added_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	dated = models.DateTimeField(auto_now=True)

