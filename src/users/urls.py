from django.urls import path
from . import views


urlpatterns = [
	path('', views.adminLogin, name='admin_login'),
]