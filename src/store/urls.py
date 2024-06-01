from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
	path('', views.getTemplate, name='store'),
	path('cart/', views.getTemplate, name='cart'),
	path('checkout/', views.getTemplate, name='checkout'),

	path('update_item/', views.updateItem, name='update_item'),
	path('process_order/', views.processOrder, name='process_order'),


	path('search_handle/', views.searchHandling, name='search_handle'),


	path('logout/', LogoutView.as_view(), name='log_out'),
]

