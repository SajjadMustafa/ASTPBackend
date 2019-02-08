from django.contrib import admin
from astpinv.models import Department, Employee, StockEntry, Unit, Item, User, IssuanceRecord

# Register your models here.


admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(StockEntry)
admin.site.register(Unit)
admin.site.register(Item)
admin.site.register(User)
admin.site.register(IssuanceRecord)
