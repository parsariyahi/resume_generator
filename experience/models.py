from django.db import models
from prof.models import Prof
# Create your models here.

EXPERIENCE_TYPE = (
    (1, "Education"),
    (2, "Work"),
)


class Experience(models.Model):
    user_profile = models.ForeignKey(Prof, on_delete=models.CASCADE, related_name="experiences")
    job_position = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True)
    type = models.IntegerField(choices=EXPERIENCE_TYPE)
