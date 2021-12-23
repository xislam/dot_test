from django.db import models


class APIData(models.Model):
    server_number = models.CharField(max_length=10)
    modem_number = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    operator = models.CharField(max_length=60)
    data_time = models.CharField(max_length=100)
    sent = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.server_number


class URL(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name
