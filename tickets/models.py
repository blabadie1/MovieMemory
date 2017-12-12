from django.db import models
from django.utils import timezone

#def get_image_path(instance, filename):
#	return os.path.join('photos', str(instance.id), filename)

class Ticket(models.Model):
	title = models.CharField(max_length=100)
	date_seen = models.DateTimeField(default=timezone.now)
	companions = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	location = models.CharField(max_length=200)
	notes = models.TextField()
#	poster = ImageField(upload_to=get_image_path, blank=True, null=True)

def publish(self):
	self.save()

# Create your models here.
