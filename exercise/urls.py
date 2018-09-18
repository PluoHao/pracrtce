from django.conf.urls import url
from .views import *
urlpatterns = [
    # 登录
    url('^hellworld$',helloworld,name='hello'),
    #注册
    url('^login$',login,name='login'),
    #首页
    url('^index$',index,name='index'),
    #个人中心页面
    url('^personal_center$',personal,name='center'),
    # 修改个人信息
    url('^upadte_password$',password,name='password'),
    # 添加地址
    url('^address',address,name='address'),
    #注销
    url('^quit',quits,name='quit'),
]