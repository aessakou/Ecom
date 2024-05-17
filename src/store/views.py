from django.shortcuts import render


def store(request):
	return render(request, 'store/home.html', {'title': 'store',})

def cart(request):
	return render(request, 'store/cart.html', {'title': 'cart',})

def checkout(request):
	return render(request, 'store/checkout.html', {'title': 'checkout',})
