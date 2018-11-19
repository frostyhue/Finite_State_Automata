from django.conf.urls import *
from . import views
from automata.views import *


urlpatterns = [
    url(r'^$', views.main, name='index'),
]