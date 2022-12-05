from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    image = models.CharField(max_length=80)
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
