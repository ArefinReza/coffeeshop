from django.db import models

class VisitorInfo(models.Model):
    ip_address = models.GenericIPAddressField()
    city = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.country}"
