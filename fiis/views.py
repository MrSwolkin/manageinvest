from django.db.models import Sum
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Fii, Trade
from .forms import TradeForm
from django.urls import reverse_lazy

# Create your views here.
#def fii_views(request):
#    fiis = Fii.objects.all()
#    
#    return render(request, "fiis.html", {"fiis": fiis})

class FiiListView(ListView):
    model = Fii
    template_name = "fiis.html"
    context_object_name = "fiis"
    


'''def trade_views(request, pk):
    fii = Fii.objects.get(id=pk)
    trades = Trade.objects.filter(fii=fii)
    
    #somando colunas
    total_amount = trades.aggregate(Sum("amount"))["amount__sum"] or 0
    total_trade = trades.aggregate(Sum("total_trade"))["total_trade__sum"] or 0
    averange = float(total_trade / total_amount)
    
    context = {
        "fii": fii,
        "trades": trades,
        "total_amount": total_amount,
        "total_trade": total_trade,
        "averange": averange    
    }
    
    return render(request, "trades.html", context)'''


class FiiDetailView(DetailView):
    model = Fii
    template_name = "fii_details.html"
    context_object_name = "fii"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fii = self.get_object()
        trades = Trade.objects.filter(fii=fii)
        
        total_amount = trades.aggregate(Sum("amount"))["amount__sum"] or 0
        total_trade = trades.aggregate(Sum("total_trade"))["total_trade__sum"] or 0
        averange = float(total_trade / total_amount) if total_amount > 0 else 0

        context["trades"] = trades
        context["total_amount"] = total_amount
        context["total_trade"] = total_trade
        context["averange"] = averange

        return context


class NewTradeCreateView(CreateView):
    model = Trade
    form_class = TradeForm
    template_name = "new_trade.html"
    success_url = "/all_trades_list/"
    


class TradesListView(ListView):
    model = Trade
    template_name = "trade_list.html"
    context_object_name = "trades"
    
    def get_queryset(self):
        trades = super().get_queryset().order_by("-date")

        return trades
    
class TradeUpdateView(UpdateView):
    model = Trade
    form_class = TradeForm
    template_name = "update_trade.html"
    context_object_name = "trade"
    

    def get_object(self, queryset=None):
        fii_id = self.kwargs.get("fii_pk")
        trade_id = self.kwargs.get("pk")
        return get_object_or_404(Trade, pk=trade_id, fii_id=fii_id)
    
    def get_success_url(self):
        return reverse_lazy(
            "trades", kwargs={'pk': self.get_object().fii.pk})
    

class TradeDeleteView(DeleteView):
    model = Trade
    template_name = "delete_trade.html"
    context_object_name = "trade"
    
    def get_object(self):
        fii_id = self.kwargs.get("fii_pk")
        trade_id = self.kwargs.get("pk")
        #print(f"FII ID: {fii_id}, Trade ID: {trade_id}")
        return get_object_or_404(Trade, pk=trade_id, fii_id=fii_id)
    
    def get_success_url(self) -> str:
        return reverse_lazy("trades", kwargs={'pk': self.get_object().fii.pk})

