from django.db import models


class Substances(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'am_substances'


class Laboratories(models.Model):    
    cnpj = models.CharField(max_length=18, unique=True)
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'am_laboratories'


class Meds(models.Model):
    substance = models.ForeignKey('Substances', on_delete=models.CASCADE)
    registration = models.BigIntegerField(unique=True)
    fabric_price_no_taxes = models.DecimalField(max_digits=10, decimal_places=2)
    max_sale_price_government = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'am_meds'


class LaboratoriesMeds(models.Model):
    med = models.ForeignKey('Meds', on_delete=models.CASCADE)
    laboratory = models.ForeignKey('Laboratories', on_delete=models.CASCADE)

    class Meta:
        db_table = 'am_meds_laboratories'
