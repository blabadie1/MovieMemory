from django.shortcuts import render
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy

def ticket_list(request):
	tickets = Ticket.objects.filter(date_seen__lte=timezone.now()).order_by('date_seen')
	return render(request, 'ticket_list.html', {'tickets': tickets})

def ticket_new(request):
	if request.method == "POST":
		form = TicketForm(request.POST)
		if form.is_valid():
			ticket = form.save()
			tickets = Ticket.objects.filter(date_seen__lte=timezone.now()).order_by('date_seen')
			return redirect('ticket_list')
	else:
		form = TicketForm()
	return render(request, 'ticket_edit.html', {'form': form})

class TicketDetail(generic.DetailView):
	model = Ticket

class TicketUpdate(UpdateView):
	model = Ticket
	fields = ('title', 'date_seen', 'companions', 'genre', 'location', 'notes')
	labels = {'companions': ('Fellow viewers'), 'notes': ('My thoughts'),}
	template_name_suffix = '_update'
	success_url = reverse_lazy('ticket_list')

class TicketDelete(DeleteView):
	model = Ticket
	success_url = reverse_lazy('ticket_list')
# Create your views here.
