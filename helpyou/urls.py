from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
app_name='helpyou'

urlpatterns = [
    path('', views.index),  # 첫 화면(메인페이지)
    path('signup/', views.signup, name='signup'), # 회원가입
    path('login/', auth_views.LoginView.as_view(template_name='helpyou/login.html'), name='login'), # 로그인
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # 로그아웃

]