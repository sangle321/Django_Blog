from django.shortcuts import render
from account.models import Account

def home_screen_view(request):
	
	context = {}
	account = Account.objects.all()
	context['accounts'] = account

	return render(request, "personal/home.html", context)
