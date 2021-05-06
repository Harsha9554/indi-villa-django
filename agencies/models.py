from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
