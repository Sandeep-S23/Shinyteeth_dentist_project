from django.contrib import admin
from . models import Contact, Appointment

class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email')
	list_display_links = ('id', 'name')
	search_fields = ('id', 'name', 'email')
	list_per_page = 15

admin.site.register(Contact, ContactAdmin)

class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'phone', 'schedule', 'date')
	list_display_links = ('id', 'name')
	search_fields = ('id', 'name', 'email')
	list_per_page = 15

admin.site.register(Appointment, AppointmentAdmin)	
