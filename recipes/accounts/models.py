from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pofile_upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image')

