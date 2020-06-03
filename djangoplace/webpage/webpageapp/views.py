# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.utils import timezone
from .models import Webpageclasses

# Create your views here.
def webpageview(request):
    return render(request,'webpage1.html')

