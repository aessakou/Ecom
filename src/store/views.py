from django.shortcuts import render
from .models import *


def store(request):
	products = Product.objects.all()
	context = {
		'title': 'Store',
		'products': products,
	}
	return render(request, 'store/home.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderitems = order.orderitem_set.all()
		items = order.get_order_items
		total = order.get_order_total
	else:
		orderitems = []
		items = 0
		total = 0
	context = {
		'title': 'Cart',
		'orderitems': orderitems,
		'items': items,
		'total': total,
	}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderitems = order.orderitem_set.all()
		items = order.get_order_items
		total = order.get_order_total
	else:
		orderitems = []
		items = 0
		total = 0
	context = {
		'title': 'Checkout',
		'orderitems': orderitems,
		'items': items,
		'total': total,
	}
	return render(request, 'store/checkout.html', context)
