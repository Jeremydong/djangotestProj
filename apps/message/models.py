from django.db import models


# Create your models here.
class UserMessage(models.Model):
    message_id = models.IntegerField(primary_key=True,default=0,verbose_name='主键')
    name = models.CharField(max_length=10,verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=50,verbose_name='联系地址')
    message = models.CharField(max_length=200,verbose_name='留言')

    class Meta:
        verbose_name_plural = '用户留言信息'