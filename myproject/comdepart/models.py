from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题",max_length=32,null=True)

class UserInfo(models.Model):
    """员工表"""
    name=models.CharField(max_length=16,verbose_name="姓名")
    password=models.CharField(max_length=64,verbose_name="密码")
    age=models.IntegerField(verbose_name="年龄")
    account=models.DecimalField(verbose_name="账户余额",decimal_places=2,default=0,max_digits=10)
    create_time=models.DateTimeField(verbose_name="入职时间")
    depart_id = models.ForeignKey(verbose_name='部门ID',to=Department,null=True,on_delete=models.CASCADE)
    gender_choices=(
        (1,"男"),
        (2,"女"),
    )
    gender=models.SmallIntegerField(verbose_name="性别",choices=gender_choices)
    #depart = models.ForeignKey(to=Department, to_field='id', on_delete=models.CASCADE)
