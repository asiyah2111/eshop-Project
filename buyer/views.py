from django.shortcuts import render, redirect
from seller.models import Product, Category
from Eshop.models import UserProfile
from .models import Cart, AddressDetails, Order, OrderProduct
from django.contrib import messages
import random

# Create your views here.
def home(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	cn=Cart.objects.filter(user_id=uobj.id).count()
	cat=Category.objects.all()
	pro=Product.objects.all()
	if request.method=='POST':
		search=request.POST['search']
		p=Product.objects.filter(name=search)	
		return render(request,"WelcomeBuyer.html",{'data':cat,'probj':p})
	return render(request,"WelcomeBuyer.html",{'data':cat,'probj':pro,'cnt':cn})
    
def product(request,id):
	cat=Category.objects.all()
	pro=Product.objects.all()
	pobj=Product.objects.filter(category=id)
	if request.method=='POST':
		search=request.POST['search']
		p=Product.objects.filter(name=search)
		return render(request,"WelcomeBuyer.html",{'data':cat,'probj':p})
	return render(request,"WelcomeBuyer.html",{'data':cat,'probj':pobj})

def cart(request,id):
	pobj=Product.objects.get(id=id)
	uobj=UserProfile.objects.get(user__username=request.user)
	try:
		c=Cart(product=pobj,user=uobj)
		c.save()
		messages.success(request,"product added....")
		return redirect('/buyer/home/')
	except:
		messages.error(request,"product already added.....")
		return redirect('/buyer/home/')

	
def cartdetails(request):()
    cat=Category.objects.all()
	uobj=UserProfile.objects.get(user__username=request.user)
	cobj=Cart.objects.filter(user_id=uobj.id)
	add=AddressDetails.objects.filter(user=uobj)
	p=[]
	for i in cobj:
		p.append(Product.objects.get(id=i.product_id))	
	return render(request,"CartDetails.html",{'p':p,'add':add,'data':cat})
def cartdel(request,id):
 	uobj=UserProfile.objects.get(user__username=request.user)
 	pobj=Product.objects.get(id=id)
 	c=Cart.objects.get(user=uobj,product=pobj)
 	c.delete()
 	return redirect('/buyer/cartdetails/')

def checkout(request):
	cat=Category.objects.all()
	user=UserProfile.objects.get(user__username=request.user)
	pid=request.POST.getlist('id')
	price=request.POST.getlist('price')
	qty=request.POST.getlist('qty')
	add=request.POST['add']
	address=AddressDetails.objects.get(id=add)
	total=[]
	prod=[]
	for i in range(0,len(pid)):
		total.append(float(price[i])*int(qty[i]))
		pro = Product.objects.filter(id=pid[i])
		newQty= pro[0].qty-int(qty[i])
		pro.update(qty=newQty)
		prod.append(Product.objects.get(id=pid[i]))
	grandtotal=sum(total)
	

	uobj = UserProfile.objects.get(user__username=request.user)
	catobj= Cart.objects.filter(user_id=uobj.id)
	catobj.delete()
	oid=ordercreation(grandtotal,user,qty,address,pid)
	return render(request,'orderplaced.html',{'total':grandtotal,'prod':prod ,'data':cat,'oid':oid}) 
def ordercreation(total,user,qty,add,pid):
	oid=random.randint(1,999999)
	ord=Order(order_id=oid,total=total,placedby=user,address=add)
	ord.save()
	for i in range(len(qty)):
		pro = Product.objects.get(id=pid[i])
		op=OrderProduct(order=ord,product=pro,qty=qty[i])
		op.save()
	return oid

def addressadd(request):
	cat=Category.objects.all()
	user=UserProfile.objects.get(user__username=request.user)
	add=AddressDetails.objects.filter(user=UserProfile.objects.get(user__username=request.user))
	print(add)
	if request.method=='POST':
		add1=request.POST['add1']
		add2=request.POST['add2']
		pin=request.POST['pin']
		city=request.POST['city']
		landmark=request.POST['lm']
		state=request.POST['state']
		mobile=request.POST['mobile']
		userobj=UserProfile.objects.get(user__username=request.user)
		ad=AddressDetails(addline1=add1,user=userobj,addline2=add2,pincode=pin,city=city,landmark=landmark,state=state,mobile_n=mobile)
		ad.save()
	return render(request,'profile.html',{'add':add,'data':cat,'user':user})
 