from django.db import models
from datetime import datetime
from agencies.models import Agency


class Agent(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
