from django.db import models
from django_ulid.models import default, ULIDField

class Community(models.Model):
    objects = models.Manager()
    id = ULIDField(default=default, primary_key=True, editable=False)

    parish = models.ForeignKey('Parish', on_delete=models.PROTECT)
    type = models.ForeignKey('CommunityType', on_delete=models.PROTECT)

    name = models.CharField(max_length=100)
    lng = models.DecimalField('Longitude', max_digits=15, decimal_places=8, null=True, blank=True)
    lat = models.DecimalField('Latitude', max_digits=15, decimal_places=8, null=True, blank=True)

    class Meta:
        verbose_name_plural = "communities"

    def __str__(self):
        return self.name

    def __str__(self):
        return self.parish

    def __str__(self):
        return str(self.type)

class CommunityType(models.Model):
    objects = models.Manager()
    id = ULIDField(default=default, primary_key=True, editable=False)

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Parish(models.Model):
    objects = models.Manager()

    id = ULIDField(default=default, primary_key=True, editable=False)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "parishes"

    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.code


