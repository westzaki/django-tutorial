from django.db import models

class Book(models.Model):
    name = models.CharField('name', max_length=255)
    publisher = models.CharField('publisher', max_length=255, blank=True)
    page = models.IntegerField('page', blank=True, default=0)

    def __str__(self):
        return self.name

class Impression(models.Model):
    book = models.ForeignKey(Book, verbose_name='book', related_name='impressions')
    comment = models.TextField('comment', blank=True)

    def __str__(self):
        return self.name