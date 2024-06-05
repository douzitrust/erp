from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'name', 'contact_person', 'phone_number', 'email', 'address', 
            'tax_id', 'company_registration_number', 'website', 
            'payment_terms', 'credit_limit', 'bank_account_details', 
            'notes', 'preferred_shipping_method', 'special_terms'
        ]
