from django.db import models
from lib.base_model import BaseModel
from accounts.models import Customer
from django.utils.translation import gettext_lazy as _

class Order(BaseModel):
    total_amount = models.IntegerField(verbose_name=_('total amount'))
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE, verbose_name=_('customer'))


    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
