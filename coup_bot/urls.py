"""coup_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
url(r'^start/', views.start),
url(r'^play/', views.play),
url(r'^tries_to_block/', views.tries_to_block),
url(r'^challenge/', views.challenge),
url(r'^lose_influence/', views.lose_influence),
url(r'^inquisitor/(?P<action>.*)', views.inquisitor),
url(r'^status/(?P<action>.*)', views.status),
]
