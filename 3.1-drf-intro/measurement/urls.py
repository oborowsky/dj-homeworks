from django.urls import path

from measurement.views import MeasuremenCreateAPIView, SensoListCreateAPIView, SensorRetrieveUpdateAPIView

urlpatterns = [
    path('sensors/', SensoListCreateAPIView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasuremenCreateAPIView.as_view()),
]
