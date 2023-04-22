import re
from pathlib import Path
from pprint import pprint

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        path = Path('/Users/weihan/PycharmProjects/avpilot/dummy')
        videos = list()
        for file in path.rglob('*'):
            if not file.is_file():
                continue
            if file.suffix not in ['.avi', '.mp4']:
                continue
            # match = re.search('.*\\w{2,6}-?\\d{3}.*$', file.stem)
            # match = re.search('.*(?P<porn_id>FC2-PPV-\\d+|\\w{2,6}-?\\d{3}).*$', file.stem, re.IGNORECASE)
            match = re.search('.*(FC2-PPV-\\d+|\\w{2,6}-?\\d{3}).*$', file.stem, re.IGNORECASE)
            if not match:
                continue
            result = {
                'path': file,
                'porn_id': match.group(),
            }
            videos.append(result)
        pprint(videos)
