from django.db import models


# Create your models here.
class NewsModel(models.Model):
    news_id = models.AutoField(primary_key=True)

    data_short = models.CharField(max_length=800)
    data_full = models.CharField(max_length=5000)
    header = models.CharField(max_length=100)

    date_published = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=40)

    media_type = models.CharField(max_length=40)
    media_link = models.URLField()

    views = models.IntegerField(default=0)
    # comments = models.ForeignKey   # edit later
    rating = models.DecimalField(decimal_places=5, max_digits=7)

    tags = models.CharField(max_length=5000)
