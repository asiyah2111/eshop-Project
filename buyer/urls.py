from django.urls import path
from . import views
app_name = 'buyer'
urlpatterns=[
	path('home/',views.home),
	path('product/<int:id>/',views.product,name="product"),
	path('cart/<int:id>/',views.cart,name='cart'),
	path('cartdetails/',views.cartdetails),
	path('cartdel/<int:id>/',views.cartdel,name="cartdel"),
	path('checkout/',views.checkout),
	path('profile/',views.addressadd),
]

