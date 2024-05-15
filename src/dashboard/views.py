from django.shortcuts import render

def dashboard(request):
	context = {
		'title': 'dashboard',
	}
	return render(request, 'dashboard/base.html', context)


def dashboardp(request):
	context = {
		'title': 'dashboard',
	}
	return render(request, 'dashboard/dashboardp.html', context)
