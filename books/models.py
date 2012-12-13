from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('author_detail', [self.pk])


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('book_detail', [self.pk])
