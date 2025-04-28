from django.db import models
from django.utils import timezone
from .managers import InvoiceManager

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('received', 'Received'),
    ]
    vendor = models.CharField(max_length=255)
    order_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    
    @property
    def total_cost(self):
        return sum(item.quantity * item.cost for item in self.line_items.all())
    
    def __str__(self):
        return f"PO-{self.id}"

class PurchaseOrderLineItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='line_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Cost per unit at time of purchase
    
    def __str__(self):
        return f"{self.product} x{self.quantity}"

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ]
    customer = models.CharField(max_length=255)
    invoice_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpaid')

    objects = InvoiceManager()
    
    @property
    def total_amount(self):
        return sum(item.quantity * item.price_each for item in self.items.all())
    
    def __str__(self):
        return f"INV-{self.id}"

class InvoiceLineItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price_each = models.DecimalField(max_digits=10, decimal_places=2)  # Price at time of invoice
    
    def __str__(self):
        return f"{self.product} x{self.quantity}"