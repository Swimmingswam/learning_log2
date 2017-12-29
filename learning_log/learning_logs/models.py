#-*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):  #定义Topic模型
	text = models.CharField(max_length=200)  #话题text属性
	date_added = models.DateTimeField(auto_now_add=True)  #话题自动添加时间
	owner = models.ForeignKey(User,1)
	def __str__(self):         
		return self.text   #告诉Django应该使用text属性来显示有关主题
class Entry(models.Model):
	topic = models.ForeignKey(Topic,1)  #与上面的Topic成一对多关系
	text = models.CharField(max_length=200)  #定义text属性
	date_added = models.DateTimeField(auto_now_add=True)  #自动添加时间
	class Meta:  #用于储存管理模型的额外信息
		verbose_name_plural = 'entries'   #告诉django使用entries表示多个Entry
	def __str__(self):
		return self.text[:50]+'...'    #告诉Django应该使用text前50字符来显示有关内容