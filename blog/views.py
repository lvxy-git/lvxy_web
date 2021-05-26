# -*- encoding=utf8 -*-
from django.shortcuts import render

# Create your views here.
from blog.models import User


def index_unlog(request):
    return render(request,'index_unlog.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = User.objects.filter(username=user_name)  # 查看数据库里是否有该用户名
        if user:  # 如果存在
            user = User.objects.get(username=user_name)  # 读取该用户信息
            if pass_word == user.password:  # 检查密码是否匹配
                request.session['IS_LOGIN'] = True
                request.session['nickname'] = user.nickname
                request.session['username'] = user_name
                return render(request, 'index.html', {'user': user})
            else:
                return render(request, 'login.html', {'error': '密码错误!'})
        else:
            return render(request, 'login.html', {'error': '用户名不存在!'})
    else:
        return render(request, 'login.html')

def logsuccess(request):
    return render(request,'index.html')