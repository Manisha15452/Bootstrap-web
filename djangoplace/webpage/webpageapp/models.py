from django.db import models
from django.conf import settings

class Webpageclasses(models.Model):
    title = models.TextField(max_length=254)
    body = models.TextField()
    text = models.CharField(max_length=200)



