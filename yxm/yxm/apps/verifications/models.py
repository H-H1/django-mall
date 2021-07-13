from django.db import models

# Create your models here.
from yxm.utils.models_time import BaseModel


class SmsSendlog(BaseModel):
    mobile=models.CharField(verbose_name='手机号',max_length=11)
    code=models.CharField(verbose_name='验证码',max_length=10)

    class Meta:
        db_table="tb_sms_send_log"
        verbose_name="短信发送记录"
        verbose_name_plural=verbose_name
        ordering=['-create_time']

