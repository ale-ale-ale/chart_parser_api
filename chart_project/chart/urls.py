from django.urls import path

from .views import SongView, ChartView

app_name = 'chart'

urlpatterns = [
    path('chart/', ChartView.as_view(), name='chart'),
    path('chart/<int:position>/', SongView.as_view(), name='song')
]