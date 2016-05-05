from .models import Rater
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        c = CopyMapping(
            # Give it the model
            Rater,
            # The path to your CSV
            '/davidmohrmann/Homework/movieratings/Data/u.user.csv',
            # And a dict mapping the  model fields to CSV headers
            dict(user_id='ID', age='AGE', gender='GENDER', occupation='OCCUPATION', zip_code='ZIP')
        # Then save it.
        c.save()
