from django.contrib import admin
from .models import Supplier, Product, NetworkNode

class ProductInline(admin.StackedInline):  # Используйте StackedInline или TabularInline в зависимости от предпочтений
    model = Product
    extra = 1  # Количество дополнительных форм для добавления продуктов

class SupplierAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

class NetworkNodeAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ['name', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'debt', 'created_at', 'node_type', 'parent_node']
    list_filter = ['city']
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность у выбранных звеньев"

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product)
admin.site.register(NetworkNode, NetworkNodeAdmin)
