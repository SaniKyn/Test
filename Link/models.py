from django.db import models


class LinkMapping(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10, unique=True, db_index=True)
    creation_date = models.DateTimeField('creation date')