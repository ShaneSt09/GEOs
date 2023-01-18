from django.db import models


class Community(models.Model):
    objects = models.Manager()

    parish = models.ForeignKey('Parish', on_delete=models.PROTECT)
    type = models.ForeignKey('CommunityType', on_delete=models.PROTECT)

    name = models.CharField(max_length=100)
    lng = models.DecimalField('Longitude', max_digits=15, decimal_places=8, null=True, blank=True)
    lat = models.DecimalField('Latitude', max_digits=15, decimal_places=8, null=True, blank=True)

    def __str__(self):
        return self.name

class CommunityType(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Parish(models.Model):
    objects = models.Manager()

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name