#-*-coding:utf-8-*-
from .models import Topic,Entry
from django import forms
class TopicForm(forms.ModelForm):
	class Meta:   #告诉Django根据哪个模型创建表单和表单中包含哪些字段
		model = Topic  #根据Topic创建表单
		fields = ['text']  #这个表单只包含text字段
		labels = {'text':''}  #告诉Django不为text生成标签
class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']  #这个表单只包含text字段
		labels = {'text':''}  #告诉Django不为text生成标签
		widgets = {'text':forms.Textarea(attrs={'cols':80})}  #添加html小部件textarea并设置宽度80