"""hotelguide URL Configuration

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
from django.urls import path,include
from django.conf.urls import url
# Add this import
from django.contrib.auth import views as auth_views
from hotels.forms import LoginForm

urlpatterns = [
    path('webadmin/', admin.site.urls),
    path('', include('hotels.urls')),
    path('', include('bookings.urls')),
    path('user', include('userprofile.urls')),
    url(r'^dashboard/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^login/$',  auth_views.login, {'template_name': 'login.html','authentication_form': LoginForm}),
    url(r'^dashboard/logout/$', auth_views.logout, {'next_page': '/dashboard/login'}), 
    # url(r'^user/profile/$', include('userprofile.urls', namespace='userprofile')),
    # url(r"^account/", include("account.urls")),
]
