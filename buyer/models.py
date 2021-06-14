from django.db import models
from Eshop.models import UserProfile
from seller.models import Product
class Cart(models.Model):
	class Meta():
		unique_together= ('user','product')
	user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

class AddressDetails(models.Model):
	addline1=models.CharField(max_length=100)
	addline2=models.CharField(max_length=100)
	pincode=models.IntegerField()
	city=models.CharField(max_length=100)
	landmark=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	mobile_n=models.CharField(max_length=13)
	user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

class Order(models.Model):
	order_id=models.CharField(max_length=100)
	date=models.DateTimeField(auto_now=True)
	total=models.DecimalField(max_digits=10, decimal_places=2)
	amt_status=models.IntegerField(default=0)
	placedby=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
	address=models.ForeignKey(AddressDetails,on_delete=models.CASCADE)

class OrderProduct(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	qty=models.IntegerField()
	status=models.IntegerField(default=0)
	