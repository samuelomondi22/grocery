from django.db import models

# Created the groceries table to hold the groceries
class groceries(models.Model):
    item = models.CharField(max_length=100)
    walmart_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    broulims_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    albertsons_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)