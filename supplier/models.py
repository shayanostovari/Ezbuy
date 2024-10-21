from django.db import models
from lib.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

class Supplier(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    address = models.TextField(max_length=120, verbose_name=_('address'))
    rate = models.SmallIntegerField(blank=True, verbose_name=_('rate'))

    class Meta:
        verbose_name = _('supplier')
        verbose_name_plural = _('suppliers')
