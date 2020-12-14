from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import SongInChart

from .serializers import SongSerializer


class ChartView(ListAPIView):
    """
    Returns List of songs in chart.
    """
    serializer_class = SongSerializer
    queryset = SongInChart.objects.all()


class SongView(RetrieveAPIView):
    """
    Returns song details for requested position.
    """
    serializer_class = SongSerializer

    def get_object(self):
        return get_object_or_404(SongInChart, position=self.kwargs['position'])


