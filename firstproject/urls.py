"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import wordcount.views  # h

urlpatterns = [
    path('admin/', admin.site.urls),
    # h : ''로 url 요청오면 wordcount 폴더안 views 파일 안에 home함수 실행
    # h : 이런 path 를 home이라고 부름
    path('',wordcount.views.home,name="home"),
    path('about/',wordcount.views.about,name="about"),
    path('count/', wordcount.views.count,name="count"), 
]
