from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, UserInfoAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', UserRegistrationAPIView.as_view(), name='register'),
    path('login', UserLoginAPIView.as_view(), name='login'),
    path('logout', UserLogoutAPIView.as_view(), name='logout'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('user', UserInfoAPIView.as_view(), name='user_info'),

]