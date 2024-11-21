from django.contrib import admin
from django.urls import path, include
from . import views
from lms_back.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register(r"blog", BlogViewSet)

urlpatterns = [
    path("api/user/Register/", CreateUserView.as_view(), name="Register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls))

]