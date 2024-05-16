from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
	path('', views.adminLogin, name='admin_login'),
	path('logout/', views.logout, name='logout'),
	path('', LogoutView.as_view(template_name='users/admin_login.html'), name='logoutsure'),
]