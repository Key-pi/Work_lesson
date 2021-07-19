from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/', auth_views.PasswordResetView.as_view(
         template_name = 'password_change_done.html'),
name = 'password_change_done'
),
    #path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),

]