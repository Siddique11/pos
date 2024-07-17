from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey



# Dashboard related models
class Dashboard(models.Model):
    total_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_due = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_due = models.DecimalField(max_digits=10, decimal_places=2)
    sales_last_30_days_chart = models.TextField()
    sales_current_financial_year = models.DecimalField(max_digits=10, decimal_places=2)
    current_financial_year_sales = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock_alert = models.IntegerField()

# Product Management models
class ProductCategory(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __str__(self):
        return self.name


    

class ProductBrand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class ProductUnit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class SellingPriceGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    unit = models.ForeignKey(ProductUnit, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    variations = models.TextField()  # JSON or another appropriate field for variations
    selling_price_group = models.ForeignKey(SellingPriceGroup, on_delete=models.CASCADE)

class ProductLabel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    label = models.TextField()

# Quick POS (Sale) models
class Discount(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)
    quotation = models.BooleanField(default=False)

class SaleReturn(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    return_quantity = models.IntegerField()
    return_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# Purchase Management models
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PurchaseReturn(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    return_quantity = models.IntegerField()
    return_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# Contacts Module models
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()

class CustomerGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    group = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE)

# Expenses Module models
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expense_invoice = models.FileField(upload_to='expense_invoices/')

# Setup Module models
class Counter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Tax(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

# Report Management models
class ProfitLossReport(models.Model):
    total_profit = models.DecimalField(max_digits=10, decimal_places=2)
    total_loss = models.DecimalField(max_digits=10, decimal_places=2)
    generated_at = models.DateTimeField(auto_now_add=True)

# User Management
class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Cashier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)