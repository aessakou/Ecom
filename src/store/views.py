from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
import json

from .models import *


def store(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.get_order_items
	else:
		items = 0
	products = Product.objects.all()
	context = {
		'title': 'Store',
		'products': products,
		'items': items,
		'shipping': False,
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
		order = []
	context = {
		'title': 'Cart',
		'orderitems': orderitems,
		'items': items,
		'total': total,
		'order': order,
		'shipping': False,
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
		order = []
	context = {
		'title': 'Checkout',
		'orderitems': orderitems,
		'items': items,
		'total': total,
		'order': order,
		'shipping': False,
	}
	return render(request, 'store/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productID = data['productID']
	action = data['action']

	customer = request.user.customer
	product = Product.objects.get(id=productID)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderitem.quantity = (orderitem.quantity + 1)
	elif action == 'remove':
		orderitem.quantity = (orderitem.quantity - 1)

	orderitem.save()
	
	if orderitem.quantity == 0:
		orderitem.delete()


	return JsonResponse("Item added to cart", safe=False)