"""
URL configuration for manageinvest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from fiis.views import FiiListView, TradeDeleteView, TradesListView, NewTradeCreateView, FiiDetailView, TradeUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", FiiListView.as_view(), name="fii_list"),
    path("trades/<int:pk>/", FiiDetailView.as_view(), name="trades"),
    path("new_trade/", NewTradeCreateView.as_view(), name="new_trade"),
    path("all_trades_list/", TradesListView.as_view(), name="all_trades_list"),
    path("trades/<int:fii_pk>/<int:pk>/update/", TradeUpdateView.as_view(), name="trade_update"),
    path("trade/<int:fii_pk>/<int:pk>/delete/", TradeDeleteView.as_view(), name="trade_delete"),

]
