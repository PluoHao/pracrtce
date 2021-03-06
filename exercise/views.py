import random

from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from pymysql import DatabaseError
# Create your views here.
import logging


# 登陆
def helloworld(request):
    if request.method == 'GET':
        return render(request,'hello.html')
    elif request.method == 'POST':
        uname = request.POST['name']
        upassword = request.POST['password']
        name = USER.objects.filter(uname__exact=uname)
        try:
            for x in name:
               if uname == x.uname and check_password(upassword,x.upassword):
                    request.session['name'] = uname
                    request.session['id'] = x.id
                    return redirect('index')
            else:
                return redirect('login')
        except DatabaseError as e:
            logging.warning(e)
            return HttpResponse('等待处理')



# 注册
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        obj = USER()
        name = request.POST['name']
        uname = USER.objects.filter(uname=name)
        if not uname:
            obj.uname = name
        try:
            password = request.POST['password']
            obj.upassword = make_password(password)
            obj.uphone = request.POST['phone']
            obj.identity = request.POST['identity_card']
        except DatabaseError as e:
            logging.warning(e)
            maggs = '数据错误'
            return render('login',locals())
        obj.save()
    return redirect('hello')

def index(request):
    try:
        user = request.session.get('name')
        return render(request,'index.html',locals())
    except DatabaseError as e:
        logging.warning(e)
        return HttpResponse('''请登录<a href="{url 'hello' }">登录</a>''')

def personal(request):
    user = request.session.get('name')
    name = USER.objects.filter(uname=user)
    addr = Address.objects.filter(USER_id=request.session.get('id'))
    for x in name:
        phone = x.uphone
        phone = phone[0:3]+"*****"+phone[len(phone)-3:len(phone)]
        sname = x.uname
        password = x.upassword
        identity = x.identity
        identity = identity[0:6]+'******'+identity[len(identity)-4:len(identity)]
    return render(request,'personal_center.html',locals())


def password(request):
    name = request.session.get('name')
    try:
        uname = USER.objects.get(uname=name)
        if request.POST.get('name'):
            uname.uname = request.POST.get('name')
            request.session['name'] = request.POST.get('name')
        elif request.POST.get('password'):
            uname.upassword = make_password(request.POST.get('password'))
        elif request.POST.get('identity'):
            uname.identity = request.POST.get('identity')
        elif request.POST.get('phone'):
            uname.uphone = request.POST.get('phone')
    except DatabaseError as e:
        logging.warning(e)
        return redirect('center')
    uname.save()
    return redirect('center')

def address(request):
    if request.method == 'GET':
        return render(request,'address.html')
    elif request.method == 'POST':
        try:
            addr = Address()
            addr.Aname = request.POST['name']
            addr.Aphone = request.POST['phone']
            addr.ADS = request.POST['address']
            s = ''
            for x in range(20):
                s += str(int(random.random() * 10))
            print(s)
            addr.orderId = s
            addr.USER_id = request.session['id']
        except DatabaseError as e:
            logging.warning(e)
            return render(request,'address.html')
        addr.save()
        return redirect('index')

def quits(request):
    try:
        s = request.session.get('name')
        del s
    except DatabaseError as e:
        logging.warning(e)
        return redirect('hello')
    return HttpResponse('你已退出{}'.format(request.session.get('name')))

