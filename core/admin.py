from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(devolucion_solicitada=False, devolucion_garantizada=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'estatus_entregado',
                    'recibido',
                    'devolucion_solicitada',
                    'devolucion_garantizada',
                    'envio_direccion',
                    'factura_direccion',
                    'pago',
                    'cupon'
                    ]
    list_display_links = [
        'user',
        'envio_direccion',
        'factura_direccion',
        'pago',
        'cupon'
    ]
    list_filter = ['ordered',
                   'estatus_entregado',
                   'recibido',
                   'devolucion_solicitada',
                   'devolucion_garantizada']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'calle',
        'municipio',
        'pais',
        'codigo_postal',
        'direccion_tipo',
        'default'
    ]
    list_filter = ['default', 'direccion_tipo', 'pais']
    search_fields = ['user', 'calle', 'municipio', 'codigo_postal']

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)