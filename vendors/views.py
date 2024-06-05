from django.shortcuts import render, redirect
from .forms import SupplierForm
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')  # Adjust this to the appropriate view
    else:
        form = SupplierForm()
    
    return render(request, 'vendors/add_supplier.html', {'form': form})


from .models import Supplier

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'vendors/supplier_list.html', {'suppliers': suppliers})