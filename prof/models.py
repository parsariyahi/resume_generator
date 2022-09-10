from django.db import models
from user.models import User
# Create your models here.


class Prof(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    title = models.CharField(max_length=150)
    job_position = models.CharField(max_length=150)
    bio = models.TextField()
    profile_img = models.ImageField()
