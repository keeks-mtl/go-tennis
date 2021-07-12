from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem, LessonLineItem


def update_on_save(sender, instance, **kwargs):
    instance.order.update_total()


post_save.connect(update_on_save, sender=OrderLineItem)
# post_save.connect(update_on_save, sender=LessonLineItem)

# @receiver(post_save, sender=OrderLineItem)
# def update_on_save(sender, instance, created, **kwargs):
#     """
#     Update order total on lineitem update/create
#     """
#     instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
