from django.conf.urls import include, url
from .views import news_page


urlpatterns = [
    url(r'$', news_page, name='fullNews'),
]