import os

from django.urls import path

from module.runtracking import views

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = [
    path('', views.RunningTrackingView.as_view(), name='home'),
]
