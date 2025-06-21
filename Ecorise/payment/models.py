from django.db import models
from trader import Trader
from recycler import Recyclers

class Payment(models.Model):
    payment_id = models.CharField(max_length=10, primary_key=True)
    trader = models.ForeignKey('Trader', on_delete=models.CASCADE, db_column='trader_id')
    recycler = models.ForeignKey('Recycler', on_delete=models.CASCADE, db_column='recycler_Id')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=30, default='M-Pesa')
    payment_status = models.CharField(max_length=30, choices=[
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    ], default='Pending')
    phone_number = models.BigIntegerField()
    mpesa_receipt_number = models.CharField(max_length=100, blank=True, null=True)
    paid_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'payment'
        unique_together = (('payment_id', 'trader', 'recycler'),)
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
    def __str__(self):
        return f"Payment {self.payment_id} - {self.amount} by {self.trader}"

