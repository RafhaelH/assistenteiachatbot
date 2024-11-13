from django.urls import path
from django.contrib.auth import views as auth_views 
from accounts.views import RegisterView



urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
