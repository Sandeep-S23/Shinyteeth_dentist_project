from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
	return render(request, 'website/index.html', {})

def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# sending an email
		send_mail(
			'You have a new mail from: ' + message_name, # subject
			message, # message
			message_email, # from mail
			['<email-id-1>','<email-id-2>'], # to mail
			)
		return render(request, 'website/contact.html', {'message_name': message_name})
	else:	
		return render(request, 'website/contact.html', {})	


def about(request):
	return render(request, 'website/about.html', {})

def pricing(request):
	return render(request, 'website/pricing.html', {})

def service(request):
	return render(request, 'website/service.html', {})				

def appointment(request):
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']

		# sending an email
		msg = "Name : " + your_name + "\nPhone Number : " + your_phone + "\nEmail ID : " + your_email + "\nAddress : " + your_address + "\nRequested Time : " + your_schedule + "\nDate : " + your_date + "\nMessage/Reason of visit : " + your_message
		
		send_mail(
			'You have a new appointment request : ', # subject
			msg, # message
			your_email, # from mail
			['<email-id-1>','<email-id-2>'], # to mail
			)
			
		param = {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_message': your_message,
		}								
		return render(request, 'website/appointment.html', param)
	else:	
		return render(request, 'website/index.html', {})
