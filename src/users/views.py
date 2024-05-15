from django.shortcuts import render

def adminLogin(request):
	context = {
		'title': 'Admin Login',
	}
	return render(request, 'users/admin_login.html', context)
