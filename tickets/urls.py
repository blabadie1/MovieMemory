from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ticket_list, name='ticket_list'),
	url(r'^ticket/new/$', views.ticket_new, name='ticket_new'),
	url(r'^ticket/(?P<pk>\d+)$', views.TicketDetail.as_view(), name="ticket_detail"),
	url(r'^ticket/(?P<pk>\d+)/update/$', views.TicketUpdate.as_view(), name='ticket_update'),
    url(r'^ticket/(?P<pk>\d+)/delete/$', views.TicketDelete.as_view(), name='ticket_delete'),
]