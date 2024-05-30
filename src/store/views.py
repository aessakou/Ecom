from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
import json
import datetime

from .models import *
from .utils import *
	

def store(request):
	# if request.user.is_authenticated:
	# 	customer = request.user.customer
	# 	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	# 	items = order.get_order_items
	# else:
	# 	data = ProcessAnonymoseUser(request)
	# 	items = data['items']

	# products = Product.objects.all()
	# context = {
	# 	'title': 'Store',
	# 	'products': products,
	# 	'items': items,
	# 	'shipping': False,
	# }
	# return render(request, 'store/home.html', context)
	return mainprocess(request, 'home')


def cart(request):
	return mainprocess(request, 'cart')


def checkout(request):
	return mainprocess(request, 'checkout')




def updateItem(request):
	data = json.loads(request.body)
	productID = data['productID']
	action = data['action']

	if request.user.is_authenticated:
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
		response = "Item added to cart"
	else:
		cart = data['cart']
		try:
			if action == 'add':
				cart[productID]['quantity'] += 1
			elif action == 'remove':
				cart[productID]['quantity'] -= 1
				if cart[productID]['quantity'] <= 0:
					newcart = {}
					for i in cart:
						if i != productID:
							newcart[i] = cart[i]
					cart = newcart
					
		except:
			if action == 'add':
				cart[productID] = {'quantity': 1}

		response = cart

	return JsonResponse(response, safe=False)


def processOrder(request):

	transactionID = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = data['form']['total']
		order.transaction_id = transactionID

		if total == order.get_order_total:
			order.complete = True
		
		order.save()

		if order.shipping == True:
			ShippingAdress.objects.create(
				customer=customer,
				order=order,
				address=data['shipping']['address'],
				city=data['shipping']['city'],
				state=data['shipping']['state'],
				zipcode=data['shipping']['zipcode'],
				phonenumber=data['shipping']['phonenumber'],
			)
	else:
		pass

	return JsonResponse("Payment complete!", safe=False)


