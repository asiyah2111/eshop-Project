from django.shortcuts import render, redirect
from .models import Category, Product
from Eshop.models import UserProfile
# Create your views here.
def home(request):
	return render(request,'WelcomeSeller.html')
def add_product(request):
	cat1=Category.objects.all()
	if request.method=="POST":
		nm=request.POST['name']
		desc=request.POST['desc']
		price=request.POST['price']
		qty=request.POST['qty']
		cat=request.POST['cat']
		img=request.FILES['img']
		cobj=Category.objects.get(id=cat)
		uobj=UserProfile.objects.get(user__username=request.user)
		pobj=Product(name=nm,desc=desc,price=price,added_by=uobj,qty=qty,category=cobj,pro_img=img)
		pobj.save()
		return redirect('/seller/add_product/')
	return render(request,'add_product.html',{'data':cat1})
