"""
URL configuration for amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from swiggy.views import home ,first ,page,second ,third,fourth ,console ,calculator,net,recv_task,task_delete,is_put
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('d',home, name='home'),
    path('f',first, name='menu'),
    path('g',page,),
    path('h',second),
    path('i',third, name='task'),
    path('v',fourth),
    path('c',console),
    path('cal',calculator),
    path('net',net),
    path('recv',recv_task),
    path('task_delete',task_delete),
    path('is_put',is_put)
   
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
