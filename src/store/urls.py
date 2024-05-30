from django.urls import path
from . import views



urlpatterns = [
	path('', views.getTemplate, name='store'),
	path('cart/', views.getTemplate, name='cart'),
	path('checkout/', views.getTemplate, name='checkout'),

	path('update_item/', views.updateItem, name='update_item'),
	path('process_order/', views.processOrder, name='process_order'),
]

