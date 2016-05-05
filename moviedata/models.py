from django.db import models

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
class Rater(models.Model):
    user_id = models.IntegerField(max_length=3)
    age = models.IntegerField(max_length=3)
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=200)
    zip_code = models.IntegerField(max_length=3)


class Movie(models.Model):
    movie_id = models.IntegerField(max_length=4)
    movie_title = models.CharField(max_length=200)
    release_date = models.IntegerField(max_length=4)
    video_release_date = models.DateTimeField
    imdb_url = models.CharField(max_length=300)

#ForeignKey is relational to another class object

class Rating(models.Model):
    user_id = models.ForeignKey('Rater')
    movie_id = models.ForeignKey('Movie')
    rating = models.IntegerField(max_length=1)
    timestamp = models.IntegerField(max_length=9)
