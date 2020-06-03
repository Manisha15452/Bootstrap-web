

from django.conf.urls import url
from .models import Webpageclasses
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url(r'^$', views.webpageview,name='webpageview'),

]
urlpatterns += staticfiles_urlpatterns()