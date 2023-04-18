from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    Me,
    Users,
    PublicUser,
    UserReviews,
    ChangePassword,
    LogIn,
    LogOut,
    JWTLogIn,
    GithubLogin,
    KakaoLogin,
)

urlpatterns = [
    path("me/", Me.as_view()),
    path("", Users.as_view()),
    path("change-password/", ChangePassword.as_view()),
    path("log-in/", LogIn.as_view()),
    path("log-out/", LogOut.as_view()),
    path("token-login/", obtain_auth_token),
    path("jwt-login/", JWTLogIn.as_view()),
    path("@<str:username>/", PublicUser.as_view()),
    path("github/", GithubLogin.as_view()),
    path("kakao/", KakaoLogin.as_view()),
    path("@<str:username>/reviews/", UserReviews.as_view()),
]
