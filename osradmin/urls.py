"""adminOSR URL Configuration

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
from osradmin.views import NotificationView
from . import views

urlpatterns = [
    url(r'^connexion/$', views.connexion, name="url_connexion"),
    url(r'^deconnexion/$', views.deconnexion, name="url_deconnexion"),
    url(r'^notification/$', NotificationView.as_view(), name="notification"),
    url(r'^ajout-d-un-membre/$', views.userAdd, name="url_useradd"),
    url(r'^liste-des-membre/$', views.userlist, name="url_userlist"),
    url(r'^ajout-categorie/$', views.addCategorie, name="url_addcategorie"),
    url(r'^ajout-langage/$', views.addLangage, name="url_addlangage"),
]
