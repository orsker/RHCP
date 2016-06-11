"""rhcp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from rhcp_core.views import index
from rhcp_core.testdata import testdata

from rhcp_client.views import client
from rhcp_client.profile import c_login, c_logout, c_reg, c_changepasswd, c_restorepasswd, c_profile, c_info
from rhcp_client.domains import c_domains, c_r01_reg
from rhcp_client.sites import c_sites

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
	url(r'^testdata/', testdata, name='testdata'),
	
	url(r'^client/', client, name='client'),
	url(r'^c_login/', c_login, name='c_login'),
	url(r'^c_logout/', c_logout, name='c_logout'),
	url(r'^c_reg/', c_reg, name='c_reg'),
	url(r'^c_changepasswd/', c_changepasswd, name='c_changepasswd'),
	url(r'^c_restorepasswd/', c_restorepasswd, name='c_restorepasswd'),
	url(r'^c_profile/', c_profile, name='c_profile'),
	url(r'^c_info/', c_info, name='c_info'),
	
	url(r'^c_domains/', c_domains, name='c_domains'),
	url(r'^c_r01_reg/', c_r01_reg, name='c_r01_reg'),
	
	url(r'^c_sites/', c_sites, name='c_sites'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
