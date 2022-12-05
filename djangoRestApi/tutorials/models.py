from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.TextField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    published = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    last_updated = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        db_table = "App_Tutorials"
