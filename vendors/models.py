from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    company_registration_number = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    payment_terms = models.CharField(max_length=100, blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bank_account_details = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    preferred_shipping_method = models.CharField(max_length=100, blank=True, null=True)
    special_terms = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
