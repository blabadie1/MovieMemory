from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ticket_list, name='ticket_list'),
	url(r'^ticket/new/$', views.ticket_new, name='ticket_new'),
]