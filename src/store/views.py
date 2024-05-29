from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
import json
import datetime

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
		try:
			cart = json.loads(request.COOKIES['cart'])
		except:
			cart = {}
		
		orderitems = []
		items = 0
		total = 0
		order = []
		for i in cart:
			items += cart[i]['quantity']

			print('cart[item]=', cart[i])
			product = Product.objects.get(id=i)
			total += (product.price * cart[i]['quantity'])


			item = {
				'product': {
					'id':product.id,
					'name':product.name,
					'price':product.price,
					'image':product.image,
					'imageURL':product.imageURL,
				},
				'quantity':cart[i]['quantity'],
				'total_cost':(product.price * cart[i]['quantity']),
			}

			orderitems.append(item)

	
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
		print(cart)
		response = cart

	return JsonResponse(response, safe=False)


def processOrder(request):
	print("Data =", request.body)

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


