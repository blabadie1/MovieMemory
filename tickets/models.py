from django.db import models
from django.utils import timezone

#def get_image_path(instance, filename):
#	return os.path.join('photos', str(instance.id), filename)

class Ticket(models.Model):
	title = models.CharField(max_length=100)
	date_seen = models.DateTimeField()
	companions = models.CharField(max_length=100, null=True)
	genre = models.CharField(max_length=50)
	location = models.CharField(max_length=200)
	notes = models.TextField(max_length=215)

	def __str__(self):
		return self.title


def publish(self):
	self.save()

# Create your models here.
