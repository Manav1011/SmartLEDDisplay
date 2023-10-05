"""
URL configuration for dynamic_led_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import index,load_rs232
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('test/',TemplateView.as_view(template_name='test.html'),name='index'),
    path('consumer/',TemplateView.as_view(template_name='consumer.html'),name='consumer'),
    path('dashboard/',TemplateView.as_view(template_name='dashboard.html'),name='dashboard'),
    path('rs232/<str:width>/<str:height>',load_rs232,name='rs232')
]
