from rest_framework import serializers

from measurement.models import Measurement, Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']
