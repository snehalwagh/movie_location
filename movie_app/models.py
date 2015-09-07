from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    fun_facts = models.TextField(blank=True, null=True)
    production_company = models.CharField(max_length=255, blank=True, null=True)
    distributor = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=128, blank=True, null=True)
    writer = models.CharField(max_length=128, blank=True, null=True)
    actor1 = models.CharField(max_length=128, blank=True, null=True)
    actor2 = models.CharField(max_length=128, blank=True, null=True)
    actor3 = models.CharField(max_length=128, blank=True, null=True)
    #latitude = models.FloatField(blank=True, null=True)
    #longitude = models.FloatField(blank=True, null=True)
    #formatted_address = models.CharField(max_length=255, blank=True, null=True)

