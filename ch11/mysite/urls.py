#-*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV  # 추가

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 아래 인증 URL 3개 추가
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photo/', include('photo.urls', namespace='photo')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

