from django.db import models
from prof.models import Prof
# Create your models here.

LANGUAGES = (
    ("fa", "Farsi"),
    ("en", "English"),
    ("tr", "Turkish"),
    ("fr", "French"),
)

LANGUAGE_LEVEL = (
    (5, "⭐⭐⭐⭐⭐"),
    (4, "⭐⭐⭐⭐"),
    (3, "⭐⭐⭐"),
    (2, "⭐⭐"),
    (1, "⭐"),
)


class Language(models.Model):
    user_profile = models.ForeignKey(Prof, on_delete=models.CASCADE, related_name="languages")
    lang = models.CharField(max_length=3, choices=LANGUAGES)
    level = models.IntegerField(choices=LANGUAGE_LEVEL)
