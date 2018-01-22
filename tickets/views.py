from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm
from django.views.generic.edit import UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import requests
import json
from .serializer import TicketSerializer


@login_required
def ticket_list(request):
	tickets = Ticket.objects.filter(user=request.user).filter(date_seen__lte=timezone.now()).order_by('-date_seen')
	for tix in tickets:
		query_title = tix.title.replace(" ", "+")
		r = requests.get('https://api.themoviedb.org/3/search/movie?api_key=e0394ce8f2493e50cb44719828947079&query=' + query_title)
		json = r.json()
		json = json['results'][0]['poster_path']
		serializer = TicketSerializer(data=json)
		tix.poster_url = 'https://image.tmdb.org/t/p/w1280' + json
	return render(request, 'ticket_list.html', {'tickets': tickets})

@login_required
def ticket_new(request):
	if request.method == "POST":
		form = TicketForm(request.POST)
		if form.is_valid():
			ticket = form.save(commit=False)
			ticket.user = request.user
			ticket.save()
			tickets = Ticket.objects.filter(user=request.user).filter(date_seen__lte=timezone.now()).order_by('date_seen')
			return redirect('ticket_list')
	else:
		form = TicketForm()
	return render(request, 'ticket_edit.html', {'form': form})

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('ticket_list')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})

class TicketDetail(LoginRequiredMixin, generic.DetailView):
	model = Ticket

class TicketUpdate(LoginRequiredMixin, UpdateView):
	model = Ticket
	fields = ('title', 'date_seen', 'companions', 'genre', 'location', 'notes')
	labels = {'companions': ('Fellow viewers'), 'notes': ('My thoughts'),}
	template_name_suffix = '_update'
	success_url = reverse_lazy('ticket_list')

class TicketDelete(LoginRequiredMixin, DeleteView):
	model = Ticket
	success_url = reverse_lazy('ticket_list')
# Create your views here.
