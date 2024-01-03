from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name=""),
    path('register',views.register,name="register"),
    path('my-login',views.my_login,name="my-login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.my_logout,name="logout"),
    path('profile',views.profile,name="profile"),
]