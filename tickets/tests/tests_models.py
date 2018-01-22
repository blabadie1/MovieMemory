from django.test import TestCase
from tickets.models import Ticket

class TicketModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		#Set up non-modified object used by all test methods
		Ticket.objects.create(title='Lady Bird', date_seen = '12/30/2017 19:50', genre='Drama', location='Evanston', notes='Great film!')

	def test_title_label(self):
		ticket = Ticket.objects.get(id=1)
		field_label = ticket._meta.get_field('title').verbose_name
		self.assertEquals(field_label, 'title')