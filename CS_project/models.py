from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50) # Tämä on vain demoa varten. Älä koskaan tallenna salasanoja näin!
    comment = models.TextField(blank=True, null=True)
