from django.db import models

# Create your models here.

class BaseDataAPI(models.Model):
    destination=models.CharField(max_length=10)
    console = models.IntegerField()
    single=models.IntegerField()
    wt=models.IntegerField()

    def __str__(self):
        return self.destination

class BaseData(models.Model):
    destination=models.CharField(max_length=10)
    console = models.IntegerField()
    single=models.IntegerField()
    wt=models.IntegerField()

    def __str__(self):
        return self.destination
