from django.db import models


# Create your models here.
class Material(models.Model):
    """材料"""

    mater_code = models.CharField(max_length=10)
    mater_name = models.CharField(max_length=40)
    mater_model = models.CharField(max_length=8)
    receipt_price = models.DecimalField(max_digits=8, decimal_places=2)
    receipt_count = models.BigIntegerField()
    receipt_date = models.DateTimeField(auto_now=True)
    operator = models.CharField(max_length=12)

    def __str__(self):
        return self.mater_code
