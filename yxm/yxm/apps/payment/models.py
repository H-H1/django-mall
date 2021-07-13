from django.db import models

from orders.models import OrderInfo
from yxm.utils.models_time import BaseModel


class Payment(BaseModel):
    """支付信息"""
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单")
    trade_id = models.CharField(verbose_name="支付编号", unique=True, max_length=255, null=True, blank=True)

    class Meta:
        db_table = "tb_payment"
        verbose_name = "支付信息"
        verbose_name_plural = "支付信息"