

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)