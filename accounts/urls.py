from django.contrib.auth import views as auth_views #import this

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/' , register_attempt , name="register_attempt"),
    path('login/' , login_attempt , name="login_attempt"),
    path('token/' , token_send , name="token_send"),
    path('success/' , success , name='success'),
    path('verify/<auth_token>/' , verify , name="verify"),
    path('error/' , error_page , name="error"),
    path('logout/' , logout_page , name="logout"),


    path("password_reset", password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password/password_reset_confirm.html",  ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password/password_reset_complete.html'), name='password_reset_complete'),      
    
   
]