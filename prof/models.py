from django.db import models
from user.models import User
# Create your models here.


class Prof(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_profile"
    )
    title = models.CharField(
        max_length=150, default=None,
        null=True, blank=True,
    )
    job_position = models.CharField(
        max_length=150, default=None,
        null=True, blank=True,
    )
    bio = models.TextField(
        default=None, null=True, blank=True,
    )
    profile_img = models.ImageField(
        default=None, null=True, blank=True,
    )

    def __str__(self) :
        return self.user.username
