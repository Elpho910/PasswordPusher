from django.db import models

# Create your models here.


class TempPassword(models.Model):
    username = models.CharField(max_length=255)
    temp_password = models.CharField(max_length=255)
    expiry_date = models.DateTimeField()
