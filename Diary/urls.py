"""Diary URL Configuration

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
from core import views


from django.conf import settings

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('user-signup/', views.signup, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('show-journal/<int:pk>/', views.show_journal, name="showjournal"),
    path('delete/<int:pk>/', views.journal_delete, name="delete"),
    path('update/<int:pk>/', views.journal_update, name="update"),
    path('extra/', views.extra, name="extra"),



    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]


