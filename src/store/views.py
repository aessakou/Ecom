from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.db.models import Q
import json
import datetime

from .models import *
from .utils import *


def getTemplate(request):
	if request.path == '/':
		return mainprocess(request, 'home')
	elif request.path == '/cart/':
		return mainprocess(request, 'cart')
	elif request.path == '/checkout/':
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
		
	else:
		customer, order = QuestOrder(request, data)


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

	return JsonResponse("Payment complete!", safe=False)


def searchHandling(request):

	try:
		data = json.loads(request.body)
		contentS = data['content']
		search_words = contentS.split()
		query_obj = Q()
		for word in search_words:
			query_obj |= Q(name__icontains=word)
		products = Product.objects.all()
		results = products.filter(query_obj).distinct()
		context = {
			'title': 'Store',
			'products': products,
			'results': results,
			'contentS':contentS,
		}
	except:
		return mainprocess(request, 'home')
		
	rendered_html = render_to_string('store/search_results.html', context)

	return JsonResponse({'rendered_html': rendered_html})
	# return render(request, 'store/home.html', context)


def product_view(request, product_id):

	product = get_object_or_404(Product, pk=product_id)
	images = product.imageURL

	data = ProcessCartData(request)
	items = data['items']
	context = {
		'title': 'View',
		'product': product,
		'images':images,
		'items':items,
	}
	return render(request, 'store/view.html', context)