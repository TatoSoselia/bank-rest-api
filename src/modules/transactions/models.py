from django.db import models
from src.modules.base.models import BaseModel


# Create your models here.
class Transactions(BaseModel):
    sender = models.ForeignKey(Account, related_name="sent_transactions", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, related_name="received_transactions", on_delete=models.CASCADE)
    amount = models.FloatField()
