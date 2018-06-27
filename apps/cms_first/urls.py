from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(regex = '^$', view = views.GeneralView.as_view(), name='main')
]