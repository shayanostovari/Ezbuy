from django.db import models
from lib.base_model import BaseModel
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _

class Customer(BaseModel):
    phone_number = models.CharField(max_length=12, unique=True, verbose_name=_('phone number'))
    username = models.CharField(max_length=20, verbose_name=_('user name'))
    credit = models.IntegerField(verbose_name=_('credit'))
    total_payment_penalty = models.IntegerField(null=True, blank=True, verbose_name=_('total payment penalty'))


    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')