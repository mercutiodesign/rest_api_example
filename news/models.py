from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=1000)
    text = models.TextField()
    date = models.DateTimeField()


