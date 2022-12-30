from django.urls import path,include,re_path
from django.contrib import admin
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'', include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)