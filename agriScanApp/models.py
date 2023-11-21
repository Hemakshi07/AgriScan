from django.db import models
from django.contrib.auth.models import User


class DashboardItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
        
class aboutus(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
