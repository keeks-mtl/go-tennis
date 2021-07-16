from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem, LessonLineItem


@receiver(post_save, sender=LessonLineItem)
@receiver(post_save, sender=OrderLineItem)
@receiver(post_delete, sender=OrderLineItem)
@receiver(post_delete, sender=LessonLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem & lessonlineitem update/create/delete
    """
    instance.order.update_total()
