from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):

	class Meta:
		model = Ticket
		fields = ('title', 'date_seen', 'companions', 'genre', 'location', 'notes')
