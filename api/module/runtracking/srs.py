import math

from rest_framework import serializers

from module.runtracking.models import RunningTracking


class RunningTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningTracking
        exclude = ('user', 'updated_at')

    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        return RunningTracking.objects.create(**validated_data)
