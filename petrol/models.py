from django.db import models
import json
# Create your models here.

class Petroleum_data(models.Model):
    year= models.CharField(max_length =4)
    petroleum_product = models.CharField(max_length=100)
    sale = models.IntegerField(default = 0)
    country = models.CharField(max_length = 100)

    # def __str__(self):
    #     return json.dumps({"petroleum_product":self.petroleum_product,"year" : self.year, "sale": self.sale, "country":self.country})

    class Meta:
        verbose_name_plural = "Datum"
