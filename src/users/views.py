from django.shortcuts import render, redirect
# from django.contrib
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def adminLogin(request):
	if request.method == 'POST':
		print('####>>>>>>FROM LOGIN FORM<<<<<####')
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'You are login')
			return redirect('dashboard')
		else:
			messages.warning(request, 'Wrong username or password')
	else:
		print('####>>>>>>ITS NOT POST METHOD<<<<<####')

	context = {
		'title': 'Admin Login',
	}
	return render(request, 'users/admin_login.html', context)


def logout(request):
	context = {
		'title': 'Logout',
	}
	return render(request, 'users/logout.html', context)