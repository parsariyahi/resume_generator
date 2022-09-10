from django.db import models
from prof.models import Prof
# Create your models here.


class Project(models.Model):
    user_profile = models.ForeignKey(Prof, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=150)
    link = models.URLField()
    description = models.TextField()
