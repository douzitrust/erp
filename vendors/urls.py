from django.urls import path
from .views import add_supplier, supplier_list

urlpatterns = [
    path('add/', add_supplier, name='add_supplier'),
    path('', supplier_list, name='supplier_list'),
    # other URLs...
]


