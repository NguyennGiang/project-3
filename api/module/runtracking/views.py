from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from module.runtracking.models import RunningTracking
from module.runtracking.srs import RunningTrackingSerializer


# Create your views here.

class RunningTrackingView(generics.ListCreateAPIView):
    queryset = RunningTracking.objects.all()
    serializer_class = RunningTrackingSerializer


