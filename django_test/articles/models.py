from django.db import models
from time import time


def get_upload_file_name(instanсe, filename):
    return 'uploaded_files/%s_%s' % (str(time()).replace('.', '_'), filename)


class Article(models.Model):
    title = models.TextField(max_length=100, default='default_title')
    body = models.TextField()
    pub_date = models.DateTimeField('date published', default=0000-00-00)
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name, default='default.png')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/articles/get/%i' % self.id


class Comment(models.Model):
    first_name = models.CharField(max_length=200, default='')
    second_name = models.CharField(max_length=200, default='')
    body = models.TextField()
    pub_date = models.DateTimeField('date published', default=0000-00-00)
    article = models.ForeignKey(Article)

