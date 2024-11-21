from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from lms_back.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('lms_back.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
