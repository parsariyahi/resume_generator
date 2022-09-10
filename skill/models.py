from django.db import models
from prof.models import Prof
# Create your models here.


class Skill(models.Model):
    user_profile = models.ForeignKey(Prof, on_delete=models.CASCADE, related_name="skills")
    skill = models.TextField()
