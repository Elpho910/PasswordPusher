from django.db import models
import uuid

# Create your models here.


class TempPassword(models.Model):
    username = models.CharField(max_length=255)
    temp_password = models.CharField(max_length=255)
    link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    expiry_date = models.DateTimeField()
    view_count = models.IntegerField(default=0)
    max_views = models.IntegerField(default=3)
