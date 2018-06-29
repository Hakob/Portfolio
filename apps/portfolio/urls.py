from django.conf.urls import url
from .views import GeneralView, GenerallyView

urlpatterns = [
	url(regex='^$', view=GenerallyView.as_view(), name='index'),
    url(regex='^$', view=GeneralView.as_view(), name='index1')
]
