from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Transaction(models.Model):
    account = models.CharField(max_length=32)
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=24, decimal_places=2)
    date = models.DateField()
    balance = models.DecimalField(max_digits=24, decimal_places=2)
    counterparty_name = models.CharField(max_length=256, blank=True, default="")
    counterparty_account = models.CharField(max_length=32, blank=True, default="")
    description = models.CharField(max_length=1024, blank=True, default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"id: {self.id} account: {self.account} currency: {self.currency} amount: {self.amount} date: {self.date}"
