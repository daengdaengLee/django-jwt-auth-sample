from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import Hello


urlpatterns = [
    # JWT 발급
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # JWT 갱신
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # JWT 검사 (Client에서 API를 이용해 JWT 검사, Client측에서 별도 인증관련 로직 필요 없어짐)
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # JWT 인증을 요구하는 API
    path('hello/', Hello.as_view()),
]
