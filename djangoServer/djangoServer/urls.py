"""djangoServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from appname import views as app_views
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'index2/', app_views.index2),
    path(r'mypage/', app_views.mypage),
    path('write/', app_views.write_server),
    path('read/', app_views.read_server),

    url('', include('appname.urls'))
]
