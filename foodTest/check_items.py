# your_app/utils/check_items.py
from datetime import datetime, timedelta
from django.core.mail import send_mail
from .models import Inventory

def send_inventory_alerts():
    today = datetime.today().date()
    soon = today + timedelta(days=3)

    low_quantity_items = Inventory.objects.filter(quantity__lt=5)
    near_expiry_items = Inventory.objects.filter(expiry_date__lte=soon, expiry_date__gte=today)

    if low_quantity_items.exists() or near_expiry_items.exists():
        message = "📦 Inventory Alert:\n\n"

        if low_quantity_items:
            message += "🟠 Low Quantity Items:\n"
            for item in low_quantity_items:
                message += f"- {item.name} (Qty: {item.quantity})\n"

        if near_expiry_items:
            message += "\n🔴 Near Expiry Items:\n"
            for item in near_expiry_items:
                message += f"- {item.name} (Expires: {item.expiry_date})\n"

        send_mail(
            subject='⚠️ Inventory Alert Notification',
            message=message,
            from_email='hasibulislam2212@gmail.com',
            recipient_list=['hasibulislam2212@gmail.com'],  # or any admin email
        )
