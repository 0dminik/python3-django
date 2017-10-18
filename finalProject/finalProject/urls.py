"""finalProject URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from home.views import homeView
from django.conf import settings
from django.conf.urls.static import static
from registrations.views import registrationsView, registration, loginView, loging



urlpatterns = [
    url(r'^$',homeView, name='home'),
    url(r'^news/(?P<id>\d+)', include('news.urls')),
    url(r'^registration/', registrationsView, name='registration'),
    url(r'^register/', registration, name='register'),
    url(r'^login/', loginView, name='login'),
    url(r'^loging/', loging, name='loging'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

