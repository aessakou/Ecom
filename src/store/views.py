from django.shortcuts import render
from .models import *


def store(request):
	products = Product.objects.all()
	context = {
		'title': 'store',
		'products': products,
	}
	return render(request, 'store/home.html', context)

def cart(request):
	orderitems = OrderItem.objects.all()
	context = {
		'title': 'cart',
		'orderitems': orderitems,
	}
	return render(request, 'store/cart.html', context)

def checkout(request):
	return render(request, 'store/checkout.html', {'title': 'checkout',})
