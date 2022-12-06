from django.db import models
from django.utils.timezone import now

# Create your models here.
# ORM을 하기 위해서는 models.Model을 상속받아야 함. 
class Deal(models.Model):
  img_url = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  link = models.CharField(max_length=200, primary_key=True)
  reply_count = models.IntegerField()
  up_count = models.IntegerField()
  cdate = models.DateTimeField(default=now)
  
  def __str__(self):
    return f'{self.title}-{self.reply_count}-{self.up_count}--{self.cdate}'
