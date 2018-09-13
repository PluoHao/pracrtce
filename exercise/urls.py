from django.conf.urls import url
from .views import *
urlpatterns = [
    url('^hellworld$',helloworld,name='hello'),
    url('^login$',login,name='login'),
    url('^index$',index,name='index'),
    url('^personal_center$',personal,name='center'),
    url('^upadte_password$',password,name='password'),
    url('^address',address,name='address'),
]