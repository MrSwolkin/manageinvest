from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Fii, Trade
# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)

class FiiAdmin(admin.ModelAdmin):
    display_list = ("name", "total_amount")
    search_field = ("name")

admin.site.register(Fii, FiiAdmin)
admin.site.register(Trade)

