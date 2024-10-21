from django.db import models
from lib.base_model import BaseModel

class Order(BaseModel):
    total_amount = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
