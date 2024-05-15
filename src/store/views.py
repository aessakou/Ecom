from django.shortcuts import render


def store(request):
	return render(request, 'store/home.html', {'title': 'store',})
