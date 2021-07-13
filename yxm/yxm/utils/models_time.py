from django.db import models


class BaseModel(models.Model):
    create_time=models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    update_time=models.DateTimeField(verbose_name="更新时间",auto_now_add=True)

    class Meta:
        abstract=True
        #说明是抽象类 只是用来做继承用 在数据库迁移时不会创建这张表
