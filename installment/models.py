from django.db import models

from lib.base_model import BaseModel
from order.models import Order
from django.utils.translation import gettext_lazy as _


class Installment(BaseModel):
    MONTHLY = 0
    FOUR_PART = 1

    installment_type = (
        (MONTHLY, _('monthly')),
        (FOUR_PART, _('four part'))
    )
    total_amount = models.IntegerField(verbose_name=_('total amount'))
    payment_penalty = models.IntegerField(blank=True, verbose_name=_('payment penalty'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='installments', verbose_name=_('order'))
