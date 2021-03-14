from django.contrib import admin
from django.urls import path, include
from registration import views as registration_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name="logout"),
    path('', include('home.urls')),
]

admin.site.site_header = 'Wealth and Awesomeness Administration'
