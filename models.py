from django.db import models

class Resource(models.Model):
    client = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    test_standard = models.CharField(max_length=50)
    certificate = models.CharField(max_length=50)

    def __str__(self):
        return self.client



