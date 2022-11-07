from django.urls import path
from account.views import *


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('profile/',UserProfileView.as_view(), name='profile'),
    path('change-password/',UserChangePasswordView.as_view(), name='changepassword'),
    path('send-password-reset-mail/',UserPasswordResetEmailView.as_view(), name='userpasswordresetmail'),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(), name='resetpassword'),

    

]