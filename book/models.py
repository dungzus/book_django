from statistics import mode
from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(name="book_name", max_length=50)
    image = models.TextField(name="book_image")
    price = models.FloatField(name="price")
    des = models.TextField(name="description")
    pub_date = models.DateTimeField(name="date_published")

    def __srt__(self):
        return self.name
