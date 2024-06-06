from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)


	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	digital = models.BooleanField(default=False, null=True, blank=False)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name
	
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_order = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	transaction_id = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.id)
	
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for item in orderitems:
			if item.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_order_total(self):
		orderitems = self.orderitem_set.all()
		return str(sum([item.total_cost for item in orderitems]))
	
	@property
	def get_order_items(self):
		orderitems = self.orderitem_set.all()
		return str(sum([item.quantity for item in orderitems]))


class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.product.name)

	@property
	def total_cost(self):
		return self.quantity * self.product.price


class ShippingAdress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	address = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	zipcode = models.CharField(max_length=200, null=True)
	phonenumber = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

class Image(models.Model):
	image = models.ImageField(null=True, blank=True)

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
class ProductDetails(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	images = models.ManyToManyField(Image, related_name='collections')
	description = models.TextField(null=True)
	quantity_dipo = models.IntegerField(default=1, null=True, blank=True)
	shippingPrice = models.DecimalField(max_digits=7, decimal_places=2)
	shippingCities = models.JSONField(default=list)


	def __str__(self):
		return self.product.name + '(Details)'
	pass

