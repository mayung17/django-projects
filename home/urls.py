from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
    path('restrict', views.RestrictView.as_view(), name='Restrict'),
    path('login', views.LoginInterface.as_view(), name='Login'),
    path('logout', views.LogoutInterface.as_view(), name="Logout"),
    path('signup',views.SignupView.as_view(),name="Signup")
]