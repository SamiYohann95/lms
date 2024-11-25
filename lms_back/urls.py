from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup_view, login_view, logout_view, auth_status

router = DefaultRouter()
router.register(r"blog", BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api/auth_status/', auth_status, name='api-auth-status'),
    path('api/login/', login_view, name='api-login'),
    path('api/logout/', logout_view, name='api-logout'),
    path('api/register/', signup_view, name='api-register'),

]