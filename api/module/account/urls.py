import os

from django.urls import path

from module.account import views

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register')
]
