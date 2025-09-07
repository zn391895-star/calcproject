from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # 👈 default home page
    path('calculator/', views.calculator, name='calculator'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),  # 👈 apna logout_view use karo
    path('calculate/', views.calculate_expression, name='calculate'),
    # path('profile/', views.profile, name='profile'),
]





