#-*-coding:utf-8-*-
from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request,"learning_logs/index.html")
@login_required
def topics(request):
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_logs/topics.html',context)
@login_required
def topic(request,topic_id):
	topic = Topic.objects.get(id=topic_id)
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic,'entries':entries}
	return render(request,'learning_logs/topic.html',context)
@login_required
def new_topic(request):
	if request.method != 'POST':  #表单未提交
		form = TopicForm()  #返回空表单
	else:    #表单已提交
		form = TopicForm(request.POST)
		if form.is_valid():  #数据验证是否有效
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()  	 #将表单数据写入数据库
			return HttpResponseRedirect(reverse('learning_logs:topics'))  #reverse获取页面topics的url，HttpResponseRedirect将浏览器重定向去topics
	context = {'form':form}
	return render(request,'learning_logs/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':  #表单未提交
		form = EntryForm()  #返回空表单
	else:    #表单已提交
		form = EntryForm(data=request.POST)
		if form.is_valid():  #数据验证是否有效
			new_entry = form.save(commit=False)  #让Django创建一个新条目对象并存到new_entry中
			new_entry.topic = topic  
			new_entry.save()  #将表单数据写入数据库
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id])) #args包含传给new_entry中的实参
	context = {'topic':topic,'form':form} #把条目存到对应的topic中
	return render(request,'learning_logs/new_entry.html',context)
@login_required
def edit_entry(request,entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner !=request.user:
		raise Http404
	if request.method != 'POST':  #表单未提交
		form = EntryForm(instance=entry)  #返回空表单
	else:    #表单已提交
		form = EntryForm(instance=entry,data=request.POST)
		if form.is_valid():  #数据验证是否有效
			form.save()  #将表单数据写入数据库
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
	context = {'entry':entry,'topic':topic,'form':form} #把条目存到对应的topic中
	return render(request,'learning_logs/edit_entry.html',context)

