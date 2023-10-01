import datetime

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_day = models.DateField()
    short_bio = models.CharField(max_length=300, verbose_name='short biography')

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_year = models.IntegerField(default=0, verbose_name='year of published')
    short_des = models.CharField(max_length=300, verbose_name='short description')
    image = models.ImageField(verbose_name='cover image')

    def __str__(self) -> str:
        return self.title