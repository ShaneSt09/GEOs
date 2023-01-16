from django.db import models


class Community(models.Model):       
    Name = models.CharField(max_length=25, default=None, null=True, blank=True)
    Type = models.CharField(max_length=15,null=True)
    Parish = models.CharField(max_length=25,null=True)    
    ParishCode = models.CharField(max_length=25,null=True)
    Longitude = models.CharField(max_length=50, null=True, blank=True)
    Latitude = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.Name

    objects = models.Manager()