from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LogoutAPIView, SignupAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('signup/', SignupAPIView.as_view(), name='api_signup'),
    path('logout/', LogoutAPIView.as_view(), name='api_logout'),
    path('refresh/', TokenRefreshView.as_view(), name='api_refresh'),
]