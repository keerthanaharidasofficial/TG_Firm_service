from django.db import models

# Create your models here.

load_plan_choices = (
    ('CONSOLE','console'),
    ('SINGLE','single')
)
destination=(
    ('ANR','ANR'),
    ('BOM','BOM'),
    ('SUR','SUR'),
    ('JFK','JFK'),
    ('SPZ','SPZ'),
    ('BRU','BRU'),
    ('BKK','BKK'),
    ('LHR','LHR'),
    ('SIN','SIN'),
    ('HKG','HKG')
)
commodity = (
    ('RD','RD'),
    ('PD','PD'),
    ('JEW','JEW'),
    ('others','OTHERS')
)
vat_claim = (
    ('YES','yes'),
    ('NO','no')
)
class TariffEntry(models.Model):
    customer = models.CharField(max_length=40)
    load_plan=models.CharField(max_length=10,choices=load_plan_choices,default='CONSOLE')
    destination=models.CharField(max_length=10,choices=destination)
    value=models.FloatField()
    wt=models.IntegerField()
    commodity=models.CharField(max_length=10,choices=commodity)
    VAT_claim=models.CharField(max_length=3,choices=vat_claim)

    def __str__(self):
        return self.customer
class TariffData(models.Model):
    customer = models.CharField(max_length=40)
    b_charge = models.IntegerField()
    add_wt = models.IntegerField()
    add_liability = models.FloatField()
    bill_entry = models.IntegerField()
    cust_inspection = models.IntegerField()
    kp_charge = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer



