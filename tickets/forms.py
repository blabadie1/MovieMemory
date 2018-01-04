from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):

	class Meta:
		model = Ticket
		fields = ('title', 'date_seen', 'companions', 'genre', 'location', 'notes')
		widgets = {
			'date_seen': forms.TextInput(attrs={'placeholder': 'Use format "D/M/Y 19:30"'}),
			'notes': forms.TextInput(attrs={'placeholder': 'Enter what you learned, or what you liked'}),
		}
		labels = {'companions': ('Fellow viewers'), 'notes': ('My thoughts'),}