from django.shortcuts import render
from .models import Fii, Trade

# Create your views here.
def fii_views(request):
    fiis = Fii.objects.all()
    
    return render(request, "fiis.html", {"fiis": fiis})

def trade_views(request, pk):
    fii = Fii.objects.get(id=pk)
    trades = Trade.objects.filter(fii=fii)
    
    return render(request, "trades.html", {"fii": fii, "trades": trades})