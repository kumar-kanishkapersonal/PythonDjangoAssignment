from django.db import models


class PharmaSales(models.Model):
    _id = models.IntegerField(primary_key=True)
    date = models.DateField(null=False)
    m01ab = models.FloatField(null=False)
    m01ae = models.FloatField(null=False)
    n02ba = models.FloatField(null=False)
    n02be = models.FloatField(null=False)
    n05b = models.FloatField(null=False)
    n05c = models.FloatField(null=False)
    r03 = models.FloatField(null=False)
    r06 = models.FloatField(null=False)
    year = models.IntegerField(null=False)


class DrugReview(models.Model):
    _id = models.IntegerField(primary_key=True)
    condition = models.TextField(null=False)
    date = models.DateField(null=False)
    drugName = models.TextField(null=False)
    rating = models.IntegerField(null=False)
    review = models.TextField(null=False)
    uniqueId = models.BigIntegerField(null=False)
    usefulCount = models.IntegerField(null=False)
