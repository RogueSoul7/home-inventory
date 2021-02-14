from django.contrib import admin
from .models import (
    Country,
    State,
    Address,
    Company,
    ItemType,
    ItemShape,
    ItemSize,
    Item,
    InventoryLocation,
    ItemInfo
)

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Address)
admin.site.register(Company)
admin.site.register(ItemType)
admin.site.register(ItemShape)
admin.site.register(ItemSize)
admin.site.register(Item)
admin.site.register(InventoryLocation)
admin.site.register(ItemInfo)
