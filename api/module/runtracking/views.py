from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from module.runtracking.models import RunningTracking
from module.runtracking.srs import RunningTrackingSerializer


# Create your views here.

class RunningTrackingView(generics.ListCreateAPIView):
    queryset = RunningTracking.objects.all()
    serializer_class = RunningTrackingSerializer

    def get_queryset(self):
        print(self.request.user)
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatisticView(APIView):
    def get(self, request):
        queryset = RunningTracking.objects.filter(user=request.user)
        total_distance = 0
        total_time = 0
        total_calories = 0
        average_speed = 0
        for item in queryset:
            total_distance += item.distance
            total_time += item.time
            total_calories += item.caloriesBurned
            average_speed += item.avgSpeed
        data = dict(
            total_distance=total_distance,
            total_time=total_time,
            total_calories=total_calories,
            average_speed=average_speed/len(queryset) if len(queryset) != 0 else 0
        )
        return Response(data)


