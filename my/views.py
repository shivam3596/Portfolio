from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from .models import mysite, my
from .forms import ContactForm

def index(request):
	lists = mysite.objects.all()
	return render(request, 'my/portfolio.html', { 'mysites':lists })

def post_form_upload(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender= form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']
			recipients = ['shivamchauhan3596@gmail.com']
			if cc_myself:
				recipients.append(sender)
		send_mail(subject,message,sender,recipients)
		return HttpResponseRedirect('request','my/congo.html')
	else:
		form = ContactForm()
	return render(request ,'my/portfolio.html')
	
def trial(request):
	lists = mysite.objects.all()
	return render(request, 'my/congo.html', { 'mysites':lists })
