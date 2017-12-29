from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))
def register(request):
	if request.method != 'POST':  #表单未提交
		form =UserCreationForm()  #返回空表单
	else:    #表单已提交
		form = UserCreationForm(data=request.POST)
		if form.is_valid():  #数据验证是否有效
			new_user = form.save()  #将表单数据写入数据库
			authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))  #reverse获取页面topics的url，HttpResponseRedirect将浏览器重定向去topics
	context = {'form':form}
	return render(request,'users/register.html',context)