from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=150, blank=False, default="")
    description = models.CharField(max_length=500, blank=False, default="")
    published = models.BooleanField(default=False)
