from django.urls import path
from .views import TriggerSOS, HeatmapDataView

urlpatterns = [
    path('api/sos/', TriggerSOS.as_view(), name='trigger-sos'),
    path('api/heatmap/', HeatmapDataView.as_view(), name='heatmap-data'),
]
