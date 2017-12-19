from django.shortcuts import render
from django.utils import timezone
from .models import Ticket

def ticket_list(request):
	tickets = Ticket.objects.filter(date_seen__lte=timezone.now()).order_by('date_seen')
	return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

# Create your views here.
