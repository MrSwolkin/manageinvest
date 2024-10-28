from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from fiis.models import Trade, FiiInventory

def fii_inventory_update():
    fii_count = Trade.objects.all().count()
    total_amount_invested = Trade.objects.aggregate(
        total_value=Sum("total_trade")
        )["total_value"]
    FiiInventory.objects.create(
        fiis_count=fii_count,
        total_amount_invested=total_amount_invested
    )


@receiver(post_save, sender=Trade)
def fii_post_save(sender, instance, **kwargs):
    fii_inventory_update()

@receiver(post_delete, sender=Trade)
def fii_post_delete(sender, instance, **kwargs):
    fii_inventory_update()

