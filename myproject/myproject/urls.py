"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from comdepart import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #部门管理
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/del/', views.depart_del),
    path('depart/<int:nid>/edit/', views.depart_edit),
    #用户管理
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/del/', views.user_del),
    path('user/<int:nid>/edit/', views.user_edit),
]
