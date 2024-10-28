from fiis.models import FiiInventory

def fii_inventory_context(request):
    inventory = FiiInventory.objects.last()
    
    return {"inventory": inventory}