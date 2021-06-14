from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
def signup(request):
	if request.method== "POST":
		fn=request.POST['fname']
		ln=request.POST['lname']
		un=request.POST['uname']
		pwd=request.POST['pwd']
		em=request.POST['email']
		mob=request.POST['mob']
		addr=request.POST['address']
		type=request.POST['type']
		uobj=User(first_name=fn,last_name=ln,username=un,password=make_password(pwd),email= em)
		uobj.save()

		user_pro_obj=UserProfile(user=uobj,usertype=type,mobile=mob,address=addr)
		user_pro_obj.save()
		return redirect('/signup/')



	return render(request,"signup.html")

def login_call(request):
	if request.method=="POST":
		un=request.POST['uname']
		pwd=request.POST['pwd']
		user=authenticate(username=un,password=pwd)
		if user:
			login(request,user)
			u=UserProfile.objects.get(user__username=request.user)
			if u.usertype=="buyer":
				return redirect('/buyer/home/')
			elif u.usertype=="seller":
				return redirect('/seller/home/')
		else:
			return HttpResponse("<h1>invalid </h1>")
	return render(request,"login.html")
def logout_call(request):
	logout(request)
	return redirect('/login/')