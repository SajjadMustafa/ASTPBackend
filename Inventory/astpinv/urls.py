from django.conf.urls import url
from .views import DisplayDept, DisplayEmp, DisplayItem, DisplayIssuanceRecord, DisplayUnit, DisplayStockEntry, \
    DisplayUser

urlpatterns = [
    url(r'^dept/', DisplayDept.as_view(), name='display_dept'),

    url(r'^all/', DisplayEmp.as_view(), name='alldisplay_emp'),

    url(r'^stockentry/', DisplayStockEntry.as_view(), name='display_stockentry'),

    url(r'^user/', DisplayUser.as_view(), name='display_user'),

    url(r'^ir/', DisplayIssuanceRecord.as_view(), name='display_Issuance_Record'),

    url(r'^item/', DisplayItem.as_view(), name='display_item'),

    url(r'^unit/', DisplayUnit.as_view(), name='display_unit'),

]
