from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=20)
	message = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Appointment(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=400)
	schedule = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	message = models.TextField(blank=True)

	def __str__(self):
		return self.name


