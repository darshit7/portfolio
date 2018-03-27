"""portfolio URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from user_management.views import LoginView, LogoutView
from portfolio_management.views import (RoleView, DesignationView,
    OrganizationView, ProjectView)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/login/$', LoginView.as_view(), name='login'),
    url(r'^api/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/role/$', RoleView.as_view(), name="role"),
    url(r'^api/role/(?P<pk>[0-9]+)/$', RoleView.as_view(), name="role"),
    url(r'^api/designation/$', DesignationView.as_view(), name="designation"),
    url(r'^api/designation/(?P<pk>[0-9]+)/$', DesignationView.as_view(),
        name="designation"),
    url(r'^api/organization/$', OrganizationView.as_view(),
        name="organizatiom"),
    url(r'^api/organization/(?P<pk>[0-9]+)/$', OrganizationView.as_view(),
        name="organization"),
    url(r'^api/project/$', ProjectView.as_view(), name="project"),
    url(r'^api/project/(?P<pk>[0-9]+)/$', ProjectView.as_view(), name="project"),
]
