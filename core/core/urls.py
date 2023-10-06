from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib import admin

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path('^', include('library.urls')),
    #path('library/', include('library.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)