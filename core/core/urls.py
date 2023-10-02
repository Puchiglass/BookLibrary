from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls', namespace='default')),
    path('library/', include('library.urls')),
]