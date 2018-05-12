from django.conf.urls import url

from api import views

app_name = 'api'
urlpatterns = [
	#
	url('v1/register/', views.register_device, name='register_device'),
]

