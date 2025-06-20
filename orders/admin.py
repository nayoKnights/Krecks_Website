from django.contrib import admin
from .models import Flavor, Order
from django.db.models.functions import TruncDate
from django.db.models import Count


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'quantity', 'phone_number', 'created_at')  # shows created_at
    list_filter = ('created_at',)  # lets you filter orders by date
    #change_list_template = 'admin/orders/order/change_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)

        try:
            qs = response.context_data['cl'].queryset
            daily_orders = qs.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('-date')
            response.context_data['daily_orders'] = daily_orders
        except (AttributeError, KeyError):
            pass

        return response
admin.site.register(Flavor)
