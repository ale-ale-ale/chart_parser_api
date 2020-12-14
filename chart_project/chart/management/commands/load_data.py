import json
from os import remove

from scrapy.crawler import CrawlerProcess
from django.core.management.base import BaseCommand
from django.conf import settings

from chart.models import SongInChart
from chart_parser.chart_parser.spiders.spotify_scraper import SpotifyScraperSpider


class Command(BaseCommand):
    help = 'Crawling data from spotifycharts.com and rewriting it in database.'

    def handle(self, *args, **options):
        path = settings.BASE_DIR.joinpath('items.json')

        if path.exists():
            remove(path)

        process = CrawlerProcess(settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        })
        process.crawl(SpotifyScraperSpider)
        process.start()

        with open('items.json', encoding='utf-8') as f:
            data = json.load(f)

            for pos_in_chart in data[0]['position']:
                obj, created = SongInChart.objects.get_or_create(position=int(pos_in_chart))
                obj.author = data[0]['author'][int(pos_in_chart)-1]
                obj.song = data[0]['song'][int(pos_in_chart)-1]
                obj.save()





