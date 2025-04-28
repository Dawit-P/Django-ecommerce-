from django.db import models
from django.db.models import Sum, F, Q
from django.utils import timezone

class InvoiceManager(models.Manager):
    def with_totals(self):
        return self.annotate(
            total_amount=Sum(F('items__quantity') * F('items__price_each'))
        )
    
    def overdue_above_total(self, min_total):
        return self.with_totals().filter(
            Q(status='unpaid') &
            Q(due_date__lt=timezone.now().date()) &
            Q(total_amount__gt=min_total)
        )