from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings






class FoodtestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodTest'

    def ready(self):
        if settings.DEBUG:  # skip in dev
            return
        from .check_items import send_inventory_alerts
        scheduler = BackgroundScheduler()
        scheduler.add_job(send_inventory_alerts, 'interval', hours=12)
        scheduler.start()
