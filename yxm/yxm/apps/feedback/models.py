from django.db import models
from users.models import User
from yxm.utils.models_time import BaseModel
# Create your models here.
class Feedback(BaseModel):
    """
    留言反馈
    """
    content = models.CharField(max_length=255, verbose_name='留言内容')
    type = models.CharField(max_length=6, default='mobile', verbose_name='留言端')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="留言用户ID")
    username = models.CharField(max_length=20, null=True, verbose_name='用户名')
    is_deleted = models.BooleanField(default=False, verbose_name='是否阅读')

    class Meta:
        db_table = 'tb_feedback'
        verbose_name = '用户反馈'
        verbose_name_plural = verbose_name