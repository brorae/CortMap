from django.db import models


class Blog(models.Model):
    # objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.title


class Blogg(models.Model):
    # objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.title
