from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(default=500.00, max_digits=100, decimal_places=2)
	slug = models.SlugField(null=False, unique=True)

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse("product_detail", kwargs={"slug": self.slug})
	
	

class BasketItem(models.Model):
	basket = models.ForeignKey('Basket', null=True, blank=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(default=599.99, max_digits=10000, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		try:
			return str(self.basket.id)
		except:
			return self.product.title

class Basket(models.Model):
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "Basket id: %s" %(self.id)
