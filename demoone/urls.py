"""demoone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from mainsite.views import home,  Company_data, Department_data, Personal_data, Delete_data
from account.views import signin, signup, logoutUser, needhelp
from chat.views import contact, chat_post
from django.conf.urls import url
import chat.views as chat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('department/', Department_data, name="department"),
    path('department/',Department_data),
    path('personal/',Personal_data),
    path('delete/',Delete_data),

    path('signin.html/', signin, name="signin"),
    path('signup.html/', signup, name="signup"),
    path('help/', needhelp, name="help"),
    path('logout.html/', logoutUser, name="logout"),

    path('mail/', contact, name="mail"),
    path('chat/', chat_post, name="chat_post"),
    path('chat/<int:pid>/<str:del_pass>',chat_post),
    path('contact/', contact),

    url(r'^captcha', include('captcha.urls')),
    ]
