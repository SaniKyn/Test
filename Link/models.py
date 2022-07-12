from django.db import models
from django.contrib.auth.models import User

class LinkMapping(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10, unique=True, db_index=True)
    creation_date = models.DateTimeField('creation date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField()