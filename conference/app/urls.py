"""conference URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
# from django.urls import reverse
# from django.shortcuts import render,redirect
# from django.urls import reverse, reverse_lazy
# from django.contrib import auth
# from django.contrib.auth.decorators import login_required
# from django.views.generic import *
# from .models import session, Speaker
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.conf import settings
# from django.conf.urls.static import static
app_name = 'app'

urlpatterns = [
        # path('login/',views.login,name='login'),
        path('',views.index,name='index'),
        path('signup/',views.signup,name='register'),
        path('login/',views.login,name='login'),
        path('logout/',views.logout,name='logout'),
        # path('register/',views.register,name='register'),
        path('sessions/',views.SessionList.as_view(),name='session_list'),
        path('sessions/(?p<pk>[0-9]+)/',views.SessionDetail.as_view(),name='session_detail'),
        path('sessions/create/',views.session_create,name='session_create'),
        path('sessions/interested/<int:session_id>/',views.interested,name='interested'),
        path('sessions/update/<int:session_id>/',views.SessionUpdate,name='session_update'),
        path('sessions/delete/(?p<pk>[0-9]+)/',views.SessionDelete.as_view(),name='session_delete'),
        path('sessions/contact',views.contact,name='contact'),
        # # path('profile/',views.profileView.as_view(),name='profileView'),
]
