from django.shortcuts import render

def dashboard(request):
	context = {
		'title': 'dashboard',
	}
	return render(request, 'dashboard/base.html', context)
