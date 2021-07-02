from django.contrib import admin

from .models import Payment, Order, OrderProduct

# Register your models here.


class OrderProductInlne(admin.TabularInline):
    model = OrderProduct
    readonly_fields = (
        "payment",
        "user",
        "product",
        "quantity",
        "product_price",
        "ordered",
    )
    extra = 0


class OrderAmin(admin.ModelAdmin):
    list_display = [
        "order_number",
        "full_name",
        "phone",
        "email",
        "city",
        "order_total",
        "tax",
        "status",
        "ip",
        "is_ordered",
        "created_at",
    ]
    list_filter = ["status", "is_ordered"]
    search_fields = ["order_number", "first_name", "last_name", "phone", "email"]
    list_per_page = 20
    inlines = [OrderProductInlne]


admin.site.register(Payment)
admin.site.register(Order, OrderAmin)
admin.site.register(OrderProduct)
