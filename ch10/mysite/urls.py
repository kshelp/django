#-*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photo/', include('photo.urls', namespace='photo')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
