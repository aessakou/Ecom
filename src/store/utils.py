from django.shortcuts import render

import json
from .models import *


def mainprocess(request, page):
	
	dataProcessing = ProcessAnonymoseUser(request)
	context = {'title': page,'shipping': False,}

	if page == 'home':
		context['items'] = dataProcessing['items']
		context['products'] = Product.objects.all()
	else:
		context = dataProcessing

	template =  'store/' + page + '.html'
	return render(request, template, context)

def ProcessCartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderitems = order.orderitem_set.all()
		items = order.get_order_items
		total = order.get_order_total
	else:
		data = ProcessAnonymoseUser(request)
		orderitems = data['orderitems']
		total = data['total']
		items = data['items']
		order = data['order']

	context = {
		'title': 'Checkout',
		'orderitems': orderitems,
		'items': items,
		'total': total,
		'order': order,
		'shipping': False,
	}

	return context

def ProcessAnonymoseUser(request):
	
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
	
	orderitems = []
	items = 0
	total = 0
	order = {}
	for i in cart:
		try:
			items += cart[i]['quantity']

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

			if product.digital == False:
				order['shipping'] = True
		except:
			items -= 1
			pass
	context = {
		'items':items,
		'total':total,
		'order':order,
		'orderitems':orderitems,
	}
	return context