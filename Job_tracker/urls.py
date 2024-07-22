"""
URL configuration for appli_tracker project.

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
from Job_tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('appform',views.Appform, name='appform'),
    path('appformdata',views.AppFormdata, name='appformdata'),
    path('appdatadelete',views.AppDataDelete, name='appdatadelete'),
    path('appdatasendtochnage',views.AppDataSendToChange, name='appdatasendtochnage'),
    path('appdataedit',views.AppDataEdit, name='appdataedit'),
    path('signup',views.Signup, name='signup'),
    path('login',views.Login, name='login'),
    path('logout',views.Logout, name='logout'),
]
