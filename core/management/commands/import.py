import re
from pathlib import Path
from pprint import pprint

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from core.models import Video


class Command(BaseCommand):
    def handle(self, *args, **options):
        folder = Path(settings.MEDIA_ROOT)
        video_list = folder.glob('**/*.mp4')
        for video in video_list:
            path = video.relative_to(settings.MEDIA_ROOT)
            row, created = Video.objects.update_or_create(
                file=str(path)
            )
            print(row, created)
