from django.conf.urls import url
from .views import GeneralView

urlpatterns = [
    url(regex='^$', view=GeneralView.as_view(), name='index')
]
