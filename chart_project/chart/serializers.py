from rest_framework import serializers

from .models import SongInChart


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongInChart
        fields = ['author', 'song', 'position']