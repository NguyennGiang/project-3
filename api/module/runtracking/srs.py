from rest_framework import serializers

from module.runtracking.models import RunningTracking


class RunningTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningTracking
        exclude = ()
