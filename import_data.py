from moviedata.models import *
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        c = CopyMapping(
            # Give it the model
            Person,
            # The path to your CSV
            '/path/to/my/data.csv',
            # And a dict mapping the  model fields to CSV headers
            dict(name='NAME', number='NUMBER', dt='DATE')
        )
        # Then save it.
        c.save()
