from django.shortcuts import render
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm
from django.shortcuts import redirect

def ticket_list(request):
	tickets = Ticket.objects.filter(date_seen__lte=timezone.now()).order_by('date_seen')
	return render(request, 'ticket_list.html', {'tickets': tickets})

def ticket_new(request):
	if request.method == "POST":
		form = TicketForm(request.POST)
		if form.is_valid():
			ticket = form.save()
			tickets = Ticket.objects.filter(date_seen__lte=timezone.now()).order_by('date_seen')
			return render(request, 'ticket_list.html', {'tickets': tickets})
			#return render(request, 'ticket_list.html')
	else:
		form = TicketForm()
	return render(request, 'ticket_edit.html', {'form': form})
# Create your views here.
