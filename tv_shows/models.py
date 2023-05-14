from django.db import models


# Create your models here.
class Shows(models.Model):
    poster_image = models.URLField()
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.FloatField()

    def __repr__(self):
        return f"{self.title} ({self.year})"
