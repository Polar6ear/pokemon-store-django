from django.contrib import admin
from .models import OrderProduct, Payment, Order

# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'order')
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    list_display =['order_number', 'full_name', 'phone_number', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone_number', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
admin.site.register(Payment)