from django.shortcuts import render
from .models import Product


def store(request):
	products = Product.objects.all()
	context = {
		'title': 'store',
		'products': products,
	}
	return render(request, 'store/home.html', context)

def cart(request):
	return render(request, 'store/cart.html', {'title': 'cart',})

def checkout(request):
	return render(request, 'store/checkout.html', {'title': 'checkout',})
