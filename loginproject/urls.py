from django.contrib import admin
from django.urls import path, include 
import loginapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginapp.views.read, name = "read"),
    path('blog/', include('loginapp.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
