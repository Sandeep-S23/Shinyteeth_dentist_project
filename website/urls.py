from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home-page'),
	path('contact', views.contact, name='contact-page'),
	path('about', views.about, name='about-page'),
	path('pricing', views.pricing, name='pricing-page'),
	path('service', views.service, name='service-page'),
	path('appointment', views.appointment, name='appointment-page'),
]