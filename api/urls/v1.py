import os

from django.urls import path, include

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = [
    path('account/', include('module.account.urls', namespace='account')),
    path('runtracking/', include('module.runtracking.urls', namespace='runtracking')),
]
