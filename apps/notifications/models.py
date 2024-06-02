# apps/notifications/models.py
from django.db import models
from apps.orders.models import Order

class Notification(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for Order {self.order.id}"

