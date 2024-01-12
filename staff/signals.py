from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Employee, Permission


@receiver(pre_save, sender=Employee)
def get_default_permission(sender, instance, **kwargs):
    if instance.is_admin():
        default_permission, created = Permission.objects.get_or_create(name='Admin')
        instance.permission = default_permission


@receiver(post_save, sender=Employee)
def set_default_permissions(sender, instance, created, **kwargs):
    if created:
        default_permission, created = Permission.objects.get_or_create(name='FinanceManager')
        default_permission, created = Permission.objects.get_or_create(name='Manager')
