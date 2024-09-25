from django.db import models

# Create your models here.
class Fii(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    total_amount = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Trade(models.Model):
    fii = models.ForeignKey(Fii, on_delete=models.CASCADE, related_name="trades")
    date = models.DateField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_trade = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.amount and self.price:
            self.total_trade = self.amount * self.price
        else:
            self.total_trade = 0
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"compra de {self.amount} de {self.fii.name} em {self.date} no total de {self.total_trade}"